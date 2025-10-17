# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c60116cb-3969-39af-8521-b18e459b0764 | -10.4302 | -45.0232 | 2025-10-17 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b864d409-3880-3afa-9280-d713c129048d | -2.7585 | -49.3922 | 2025-10-17 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 768f5922-459b-3024-8f15-872f67bf6f5b | -7.2137 | -45.4882 | 2025-10-17 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 1e21800b-a77d-3dbf-8df9-9007f788931b | -2.7401 | -49.3927 | 2025-10-17 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 0eed36d5-59ef-371b-8f5a-7f7427b0aaac | -5.496 | -47.308 | 2025-10-17 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 75666678-5fe0-3e1e-b9b0-8b164aca170e | -4.9548 | -44.956 | 2025-10-17 00:00:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5e26022b-3596-3b46-9a47-74d60acd83f5 | -5.5147 | -47.3069 | 2025-10-17 00:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 75caf3ea-9f23-323d-952d-90d57a2148d1 | -10.2748 | -44.0247 | 2025-10-17 00:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 5afd2720-dd7a-3a35-a35b-2ddde38a834b | -10.1528 | -44.5289 | 2025-10-17 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f69b4749-1d9a-35ac-9cc1-66df048cd5f5 | -3.2545 | -45.9855 | 2025-10-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| c470ae1c-2053-325f-be1a-b2ffe83764fd | -4.4059 | -43.4049 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 768.7 |
| 8fdad96b-9602-3995-9f25-9f3a9c4e02f4 | -4.4058 | -43.4282 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 7b325773-f58e-3545-afd8-045428f18add | -14.002 | -51.0403 | 2025-10-17 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c98b3a75-2108-318f-a548-b2bae63abb92 | -11.5733 | -48.5568 | 2025-10-17 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e3500e06-e488-3520-9c17-fe9e530f1e8e | -5.2596 | -44.2058 | 2025-10-17 00:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 10e3a871-9fba-38d3-984b-6fc4a53ec7b6 | -4.4245 | -43.4271 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3e08edad-fb8b-338a-b3e9-5cccdf79d2e3 | -10.5132 | -43.4289 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 71eb318d-45cb-3970-a35a-a85c72b768df | -4.4061 | -43.3816 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 330.6 |
| c907f049-261a-349c-af44-11c7233e70cc | -3.236 | -45.9639 | 2025-10-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 238.1 |
| e3d34f07-6f92-323e-91c1-16f327683304 | -14.0214 | -51.0377 | 2025-10-17 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ba91f8b3-4a56-3af1-9115-f978c2d16f1e | -4.4653 | -42.9346 | 2025-10-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5f79051a-7554-3a1a-878a-a50d02f43d98 | -10.514 | -43.3815 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 30ff86dd-fd6c-31d1-acf4-a40a99b27ab5 | -8.237 | -44.8213 | 2025-10-17 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5434daeb-0e5b-36cd-bf27-b17359c63fe9 | -7.1949 | -45.4899 | 2025-10-17 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 00e6f77e-2652-39fc-9205-8aca68322849 | -10.4949 | -43.3842 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5c3e1402-00e9-3d95-9069-53fae522274e | -3.9822 | -42.4924 | 2025-10-17 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 58058e49-e362-3a05-9907-0cd1ff551121 | -9.0821 | -48.0252 | 2025-10-17 00:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 5913a9e1-2dd6-3b11-9536-e4ca17ef79d6 | -10.2745 | -44.0481 | 2025-10-17 00:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| c55f5b49-1997-39de-a1b5-bc86f6483756 | -4.484 | -42.9335 | 2025-10-17 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a9c1a554-8907-35b0-9f1f-83a04fbdad44 | 1.058 | -51.2065 | 2025-10-17 00:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 066e369b-ab1d-32af-911c-fcb9e50066f2 | -11.5924 | -48.5544 | 2025-10-17 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e5cc28da-272f-33a4-a113-54334832ff37 | -7.9631 | -44.113 | 2025-10-17 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 5cf5936e-5c55-3760-abea-d42ae01c46b7 | -4.3874 | -43.3827 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1719abb5-3406-34e5-9e3f-e7e7401259b4 | -10.2935 | -44.0455 | 2025-10-17 00:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 8ad4e801-7eb1-3c32-aff4-5815a976fd94 | -4.4248 | -43.3805 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 117ae741-8585-3099-ba3d-ae7c8b8e04ab | -4.3871 | -43.4292 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9a7ce4c4-e02f-3d40-add2-1846f5c12745 | -8.1996 | -43.3189 | 2025-10-17 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 290dd6f7-481b-37c7-823d-02405928342e | -3.2359 | -45.9862 | 2025-10-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 2dccd45c-641f-36f4-b831-a79ee540af15 | -18.0898 | -42.4475 | 2025-10-17 00:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| a928905d-9f8e-3ac4-aecb-9ef07d092802 | -2.7441 | -48.3022 | 2025-10-17 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ad0ba33f-ad0f-37a2-bbcd-4f5ac75caa14 | 1.058 | -51.2272 | 2025-10-17 00:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 0fc70b92-682e-38fb-ba7d-8d59a9e0ada1 | -2.7586 | -49.371 | 2025-10-17 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 7a5f9c5b-fdb0-3e57-8606-35f3fe9f6c70 | -4.3872 | -43.406 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 045a546e-c7df-3fda-b961-44f0544de33c | -7.9442 | -44.115 | 2025-10-17 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e3b12d21-240f-35d1-aa8c-7b99f75e6652 | -9.7113 | -48.9202 | 2025-10-17 00:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 03efad75-6810-38c8-82bc-37a78f438097 | -14.021 | -51.0592 | 2025-10-17 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 5298ccfd-20b2-39f0-8e99-5438d091aa9b | -3.2546 | -45.9632 | 2025-10-17 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| a379e5f9-77a8-3499-a43e-905d3937b774 | -2.7401 | -49.3715 | 2025-10-17 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 54fc358d-8737-3a6e-9ba7-9569c39675dc | -10.4945 | -43.4079 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 260ad9a1-6af3-337d-a8d8-d03a2a936021 | -11.5917 | -44.0707 | 2025-10-17 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 7cf138ef-668d-300d-9637-5fe2e4832f84 | -10.9475 | -49.7605 | 2025-10-17 00:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b982ea90-5530-3cba-910f-d75f9c84f55c | -10.4941 | -43.4315 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 4d17b669-28eb-31e4-a103-a854103457b4 | -12.2847 | -47.1094 | 2025-10-17 00:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 925e11f8-eacf-3dfb-a498-19a00803ced1 | -10.2939 | -44.0221 | 2025-10-17 00:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 0b6630ad-c3fa-35e4-84b2-c148569568bc | -10.5136 | -43.4052 | 2025-10-17 00:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 480830c8-ee79-3435-8ecd-aa1d0ca4b0f5 | -4.4246 | -43.4038 | 2025-10-17 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 284.8 |
| 0caa1ef2-37e0-39a1-b912-abdabf5834c1 | -8.4079 | -46.2314 | 2025-10-17 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 639ffed6-572e-30ed-a507-37ae77326a82 | -19.98254 | -41.77312 | 2025-10-17 00:09:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.8 |
| 11a94f05-ed0d-32b0-b902-ca7d18ae3667 | -20.54128 | -44.07165 | 2025-10-17 00:09:00 | TERRA_M-M | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 06037de1-f90b-3789-a2b5-2597513f4c2c | -19.60618 | -41.78086 | 2025-10-17 00:09:00 | TERRA_M-M | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a21c4ba1-c3de-382d-8048-2dbafc7c26c3 | -19.60488 | -41.77154 | 2025-10-17 00:09:00 | TERRA_M-M | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| a6eff50f-365c-3c9d-8180-ceab59422ea6 | -21.02003 | -48.42569 | 2025-10-17 00:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 41.0 |
| e60ad193-2206-39d8-a24b-d6f668093eae | -19.21788 | -44.1165 | 2025-10-17 00:09:00 | TERRA_M-M | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 96ca8201-e887-30ff-a9c1-61b5853e4c79 | -19.98383 | -41.78247 | 2025-10-17 00:09:00 | TERRA_M-M | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| d827ba07-5cc2-30e7-97be-c2550880b8a6 | -18.83762 | -43.17461 | 2025-10-17 00:09:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ecfcd21a-0f3d-3f35-be47-abcaa2827d01 | -19.91121 | -45.79729 | 2025-10-17 00:09:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c42c19b0-e15d-3a49-b0df-a60c96ef1fc3 | -22.22139 | -43.33491 | 2025-10-17 00:09:00 | TERRA_M-M | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| febbeaad-940e-3c33-8251-dff7ba721863 | -21.01867 | -48.4193 | 2025-10-17 00:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 598bb7fc-31e0-33c3-99d7-039f44e3b6c7 | -22.58913 | -44.76974 | 2025-10-17 00:09:00 | TERRA_M-M | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1fd40f12-4a65-3d54-b9f9-5d4616280783 | -19.60358 | -41.76221 | 2025-10-17 00:09:00 | TERRA_M-M | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.3 |
| bfdbed84-0b59-3156-9786-9b4f1297e85c | -20.54261 | -44.0824 | 2025-10-17 00:09:00 | TERRA_M-M | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 4b4b7aa9-a095-38be-b2de-8abfc929af59 | -4.4061 | -43.3816 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 0008f63c-d5ef-3f87-9fbc-51725e81c652 | -4.3871 | -43.4292 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 70d17b05-d844-3d60-a845-cf24df8682ed | -7.9631 | -44.113 | 2025-10-17 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 85c1efcf-5ce3-3be3-95ee-49945d006cce | -4.484 | -42.9335 | 2025-10-17 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7b81c409-04ce-3ce6-b20d-e9fcb0fe826f | -7.1949 | -45.4899 | 2025-10-17 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f88f4e0a-176c-389c-9337-1e5d6941f0ce | -4.3874 | -43.3827 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 49ec3381-0e73-38e4-bf8a-3109ac3be4a4 | -11.5729 | -44.0501 | 2025-10-17 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e3876562-b684-33ad-8589-c511e855f693 | -4.4246 | -43.4038 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 2969ea68-899c-3fe7-87a6-18e5ecdc9b1e | -2.744 | -48.3238 | 2025-10-17 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 1a5ceadc-dc7c-3f62-ad2e-ca61735a01c4 | -10.4945 | -43.4079 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c2c4bd5d-d317-3acc-9288-22adfde7dcfc | -10.4302 | -45.0232 | 2025-10-17 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 15517d7c-bf2a-335b-a938-89b127fdacca | -10.2745 | -44.0481 | 2025-10-17 00:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 1b3db7af-e6be-35ad-a374-21944436b677 | -3.2545 | -45.9855 | 2025-10-17 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b44c412c-db7a-3cd9-8f44-72adf6cd2b24 | -10.2748 | -44.0247 | 2025-10-17 00:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 173.1 |
| dd61140d-0bee-3b9a-932b-6c30a12a03b7 | -11.5921 | -44.0472 | 2025-10-17 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6c011e5c-17fd-37fa-b18c-1b1cf002d5d5 | -10.4949 | -43.3842 | 2025-10-17 00:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 74561469-f228-312c-9c23-28f632cb65c8 | -4.4059 | -43.4049 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 803.3 |
| ad9984d3-2f05-3b74-a3ae-d59402906c42 | -2.7441 | -48.3022 | 2025-10-17 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 026b315f-a9ed-3474-876a-07bc07aac2d6 | -2.7586 | -49.371 | 2025-10-17 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 302e5f49-d44b-33c5-8aad-8cdbf5faf989 | -4.4058 | -43.4282 | 2025-10-17 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 70f66ab2-f144-3cfd-a7f9-afbc535001f6 | -2.7585 | -49.3922 | 2025-10-17 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2722bb5b-0faa-3698-9f62-5eefcbce8b99 | -16.0324 | -43.4953 | 2025-10-17 00:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 77982c5c-b524-32fe-ba75-00ea2c4aa77b | -7.9442 | -44.115 | 2025-10-17 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| dbe31b6b-8ca2-3366-b169-11736a0a9366 | -11.5917 | -44.0707 | 2025-10-17 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 7f151922-1de8-34d2-b637-ed1345055263 | -11.4748 | -44.1819 | 2025-10-17 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 595df229-1935-385d-b853-13f2b390aa2b | -9.898 | -47.6758 | 2025-10-17 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d6736e37-7855-3a61-9535-e4ede91da6e4 | -9.7113 | -48.9202 | 2025-10-17 00:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e96be759-64e0-337b-b5fc-0bb0953700e1 | -10.7972 | -49.6693 | 2025-10-17 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| f35f72af-dd69-3186-9dde-a9d443254855 | -10.7975 | -49.6478 | 2025-10-17 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |


[Clique aqui para ver as próximas entradas](README2.md)
