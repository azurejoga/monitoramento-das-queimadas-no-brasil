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

## Dados Diários - Página 291

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2349a98d-b010-3a3c-a079-800b93d47e73 | -10.2317 | -46.8382 | 2026-10-09 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 764a3263-00f5-3120-9294-cfceceb9049f | -15.8531 | -42.0202 | 2026-10-09 18:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 394.5 |
| d6a0a0cd-65ad-3f61-9016-3ab02b96b58b | -3.571 | -59.0777 | 2026-10-09 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a4c2f76c-4b0d-356c-aeeb-e53559f6d7be | -3.1879 | -58.6626 | 2026-10-09 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 8b8c9e4c-45f6-33ec-bb8a-c2f5b68c623b | -3.6435 | -59.3064 | 2026-10-09 18:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f2b87331-8b7e-3b04-b17b-1343d22abc0e | -3.2945 | -54.0006 | 2026-10-09 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 6c0804c3-dca6-3306-a32b-e4144ea73299 | -16.2353 | -44.053 | 2026-10-09 18:20:00 | GOES-19 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 46c1411d-4294-3cc3-ad56-8a9ee1b2ea1a | -10.4111 | -46.2551 | 2026-10-09 18:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 43fab883-af7b-3135-a374-f807e7348bb7 | -4.7404 | -55.6522 | 2026-10-09 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 22fbbe02-2a55-3b62-a22c-edfd1fab4e9b | -3.1879 | -58.6433 | 2026-10-09 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 139.0 |
| 6e53bc5c-0e87-3c6e-86f5-950d8256d240 | -7.2074 | -44.3485 | 2026-10-09 18:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d0d75159-1c54-3ac0-940c-b3fa74bcddb8 | -7.4889 | -42.8059 | 2026-10-09 18:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| b3f62e78-eab2-3773-9f8d-e05489c020b1 | -11.47 | -43.3824 | 2026-10-09 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 99ca1924-5ff8-3d4a-bf2e-503d7c98bf8d | -9.2781 | -47.4333 | 2026-10-09 18:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 39ab5bab-689d-375d-8098-aaf5c7b91253 | -15.6777 | -39.6899 | 2026-10-09 18:20:00 | GOES-19 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| b5ff780b-ed21-3d8d-9abc-ef1bbaa90afd | -12.7067 | -43.0851 | 2026-10-09 18:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 119.7 |
| ff8ed4cf-96e5-3626-a2b2-70019844e756 | -9.9398 | -43.5542 | 2026-10-09 18:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| f8710736-bde1-32e5-9c6d-328dc6cab860 | -9.8451 | -44.7757 | 2026-10-09 18:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 44c7f9d6-c3e4-301a-b33f-96b134a105cd | -9.3162 | -47.4072 | 2026-10-09 18:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 52d1071c-217d-3261-a1c0-04916d2f4323 | -16.9672 | -41.154 | 2026-10-09 18:20:00 | GOES-19 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.9 |
| c0ebb5c4-508a-3200-986b-725801f3d6e2 | -10.473 | -47.1887 | 2026-10-09 18:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| c4405154-585f-3bc7-98a3-74894ecd3b5b | -7.5073 | -46.0924 | 2026-10-09 18:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ef9bb4e1-7a79-3dc3-8c17-139e3e72f4e2 | -8.358 | -44.2101 | 2026-10-09 18:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| c2d3626e-cf28-312e-af8a-4eac2b1e4952 | -3.2532 | -50.4108 | 2026-10-09 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 28d16073-cda4-331f-b762-5b7f5ae4ab69 | -3.1972 | -50.5592 | 2026-10-09 18:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7a8decee-47f1-38bb-8d8f-5b0a74bec816 | -13.3671 | -43.8742 | 2026-10-09 18:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 427.6 |
| ee1d9f50-7ff7-331d-ac06-91f998fb8160 | -7.9406 | -47.6284 | 2026-10-09 18:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 066679f7-60c9-30dc-beb3-3cacc3ab3bcb | -12.0453 | -43.4102 | 2026-10-09 18:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 17df50a9-65d2-344f-ba78-5819d6ecbabc | -9.2973 | -47.4092 | 2026-10-09 18:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 69c67863-0587-361c-8228-03bce9a4c5bc | -2.5721 | -56.1449 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 521eba00-da5c-3d59-b650-a275670633d2 | -3.5709 | -59.0969 | 2026-10-09 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c24657f6-29f4-31e5-b005-72eb837332e3 | -9.0173 | -44.3676 | 2026-10-09 18:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 72b94f7e-0a65-39af-b897-99fb3b45a12f | -3.9511 | -55.3209 | 2026-10-09 18:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 5a91304a-440d-3515-9f16-b476508eecd0 | -3.1697 | -58.6244 | 2026-10-09 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a3a67110-abae-3a6b-ad18-7002272e60f4 | -10.4724 | -47.2333 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| ae688154-f90f-3a2a-9cc2-8db3460bbcd0 | -0.7398 | -57.9598 | 2026-10-09 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2bc8f981-37a9-3fd8-9379-6e909c157ab4 | -7.0036 | -47.7062 | 2026-10-09 18:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f0af862e-43da-3a02-8201-fd1292436d32 | -10.4914 | -47.231 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4c0518b6-5bba-3573-a28e-71a36e930fab | -2.4942 | -58.0768 | 2026-10-09 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8bf8eba3-0926-3548-82d7-dded6345416e | -2.4442 | -55.97 | 2026-10-09 18:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5db7d504-d512-30d0-8768-ee9eb53455a3 | -18.3132 | -42.365 | 2026-10-09 18:30:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 188.7 |
| d7b7d142-4048-3c33-8843-192c1b88a507 | -2.7335 | -57.4717 | 2026-10-09 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| cd29ac3c-e37b-3970-8aae-7a56e6bfac7d | -7.4976 | -45.2814 | 2026-10-09 18:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 42bbc931-e834-347b-ba54-f14244132c33 | -2.8997 | -56.9423 | 2026-10-09 18:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 785aaf19-c05a-3796-bc8e-cf67b3f33dd7 | -3.6814 | -58.8831 | 2026-10-09 18:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e5ac9bbd-4798-3a20-8244-963a56f0a144 | -12.8303 | -44.6239 | 2026-10-09 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| bfeb0e80-59a4-38ab-a3a3-d248150c9c78 | -4.0856 | -53.9969 | 2026-10-09 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 345.5 |
| ec1ce280-05b1-33bf-a341-27959847131b | -15.2732 | -42.3699 | 2026-10-09 18:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |
| 7e8acb2e-ae72-344c-8e49-d865c66682fe | -10.2488 | -49.6636 | 2026-10-09 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ff828d54-eadc-3207-af17-1bff71fbbd81 | -13.7657 | -48.1224 | 2026-10-09 18:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| cf3e6966-b8cb-392a-ac0d-9a1ee604e257 | -2.8899 | -54.0711 | 2026-10-09 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 54e37d3e-46b6-3267-a9c1-86bc678391e7 | -3.0925 | -53.9455 | 2026-10-09 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| eb7f3dab-51e1-33fd-a44d-2e8f382373d9 | -2.853 | -54.1322 | 2026-10-09 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f969125c-6b68-338c-96a7-31966a7b05f6 | -3.1059 | -50.3105 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a28da308-95af-3a7b-be9d-a474ea354384 | -1.7296 | -56.0597 | 2026-10-09 18:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ae9ae197-1fb8-3093-a58a-fe84cbd055cf | -7.3547 | -50.0272 | 2026-10-09 18:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 49a321e9-3c75-3807-8994-43ee18970d3e | -3.571 | -59.0777 | 2026-10-09 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e75a495c-78bc-3938-bf89-c444c37e34b0 | -16.2353 | -44.053 | 2026-10-09 18:30:00 | GOES-19 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 21db2cbd-ccab-3d9f-ae9a-6e91717e6c7a | -14.4541 | -43.912 | 2026-10-09 18:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 128.3 |
| ac757fa5-545e-32c3-b24a-f4d1c36c5a89 | -17.4581 | -45.0511 | 2026-10-09 18:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 8222592a-dbfd-33db-8a15-31fa8d54a89d | -4.7404 | -55.6522 | 2026-10-09 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4b54a87a-f759-31b0-83d2-8fcebd2325c4 | -3.0559 | -53.9062 | 2026-10-09 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 85940777-b74e-3868-97f4-f84b6c11ed25 | -15.4029 | -41.8985 | 2026-10-09 18:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 564.9 |
| 9540cdab-5c6a-3d90-a7d9-a7df7ce2899e | -14.4535 | -43.9359 | 2026-10-09 18:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 430.4 |
| a8fcfb07-6680-3bd1-b33f-ad2b9976a978 | -15.8531 | -42.0202 | 2026-10-09 18:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 408.8 |
| 5eeb80fb-e276-3ba3-8d53-5534274c9224 | -2.7429 | -54.0945 | 2026-10-09 18:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5112e8d1-c313-3369-b81a-44ba7ee88832 | -3.2136 | -42.9764 | 2026-10-09 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| de9fe1c8-b0a3-38a3-9472-c9498582091a | -9.8795 | -50.5131 | 2026-10-09 18:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 010dbcd9-fe1e-32b9-97eb-2adb57498ba8 | -10.4334 | -47.3046 | 2026-10-09 18:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| c11f8272-1a55-3eb7-b4a9-eb49e60ac140 | -12.0453 | -43.4102 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| e7a299e8-5715-3929-872f-49ab67f5f153 | -10.4524 | -47.3024 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 39513fb6-defa-3201-8e81-a20847bff97c | -12.0058 | -43.464 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 8437a63a-70ed-3524-93aa-48c9c9c910b3 | -7.0038 | -47.6843 | 2026-10-09 18:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ee3a6c59-bc5d-33ec-8afe-8ad50e457f4e | -6.5826 | -43.034 | 2026-10-09 18:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 49dfe1e2-5c73-393e-ad97-f4bda8148c86 | -10.3544 | -46.2396 | 2026-10-09 18:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f3e8b850-ec84-374d-9e8a-0ac5e9f2be98 | -5.5315 | -43.0498 | 2026-10-09 18:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 60259827-549c-39e7-95d9-c143103dcff8 | -3.2137 | -42.953 | 2026-10-09 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 36cb1084-9faf-3595-a6e3-6e779b238a20 | -6.4909 | -46.6 | 2026-10-09 18:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 91a0cd9b-61cf-347b-8f0a-9d8da8e2f5b5 | -13.3865 | -43.8708 | 2026-10-09 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 6e629fe0-74b3-3ca4-a696-41731aec70eb | -12.3708 | -46.5789 | 2026-10-09 18:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 38e0671f-b6ca-3b50-80a7-fff3ae6f28ea | -8.9311 | -45.1355 | 2026-10-09 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| aa667aaa-1a20-3323-b8bd-615ac060e5d5 | -10.4147 | -47.2846 | 2026-10-09 18:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 37f768a6-e247-3374-8acf-51c7bb6c5786 | -11.9673 | -43.4702 | 2026-10-09 18:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 107cae1c-75a0-32d9-b24b-b5fee50dacd0 | -12.2123 | -44.7457 | 2026-10-09 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| f7822c25-09e3-3260-ab15-1a80257253c3 | -14.0662 | -43.8424 | 2026-10-09 18:30:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 9ba6317f-bde4-36d9-9c0e-8c90703d50d4 | -3.9664 | -51.8829 | 2026-10-09 18:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b75e7a4b-89af-3866-aab1-650a6c5584bc | -2.7612 | -54.1142 | 2026-10-09 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 304277ce-be6b-3cd6-83d8-5ff373dbe764 | -7.4889 | -42.8059 | 2026-10-09 18:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 7e9159ec-d13e-3b20-ad7a-3a1ac45ed332 | -8.0952 | -45.632 | 2026-10-09 18:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ef5807e2-5b82-32ea-b003-1eaa0667209d | -3.1787 | -50.5807 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ca670008-2953-3529-9bbc-1072bb653d41 | -9.9398 | -44.7869 | 2026-10-09 18:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 9d2b00e6-ac71-3add-9229-a27b6b314c26 | -15.2535 | -42.3741 | 2026-10-09 18:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.6 |
| 49c100d6-9ce7-3a18-a744-3815e0faaf5e | -10.8905 | -44.8232 | 2026-10-09 18:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| b260cb12-41f8-3358-abd6-8c740e58cc96 | -6.2363 | -43.8562 | 2026-10-09 18:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 093fa3b3-c71d-3818-8a04-f09ae29138c8 | -2.8712 | -54.192 | 2026-10-09 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6a24e2dc-5f2a-3148-b988-28dad3ca195a | -17.4575 | -45.075 | 2026-10-09 18:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 2af93e83-c319-3e30-82c5-1a6da8828e98 | -2.9979 | -54.7692 | 2026-10-09 18:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a5cf4801-9b0f-37ad-9db0-561a09eb77a1 | -3.3455 | -50.4078 | 2026-10-09 18:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 759ed8de-f9ad-36dd-bc70-3ddcf27a2f8c | -7.5073 | -46.0924 | 2026-10-09 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| fcf68e5e-545b-37fb-a5eb-5680f540a2b8 | -4.7219 | -55.6727 | 2026-10-09 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README292.md)
