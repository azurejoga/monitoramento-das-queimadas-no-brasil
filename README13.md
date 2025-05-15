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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2804226-aeea-3cf5-89e2-0d9d4194d81a | -14.06795 | -57.10765 | 2025-05-15 05:18:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77792b48-997f-31bd-b66f-d016af228aa3 | -19.15526 | -47.81833 | 2025-05-15 05:18:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6e9c88a-ff08-349a-9b0d-1b2b66735ba5 | -16.0719 | -60.03661 | 2025-05-15 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d720f941-7f54-3ab6-ae90-317a9108c453 | -19.06112 | -53.45234 | 2025-05-15 05:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b042720-4be6-3e8e-9b35-e1bdf50cccd6 | -19.16043 | -47.81896 | 2025-05-15 05:18:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83f5f149-a5d6-32c6-84d1-6ca8e77eeab7 | -21.78287 | -52.73991 | 2025-05-15 05:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf7790db-c611-34d1-aadc-82b895bdb4e3 | -21.7796 | -52.74253 | 2025-05-15 05:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b7ba00b-08ae-3388-8596-245de51f9f00 | -23.60878 | -48.29946 | 2025-05-15 05:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 316c550d-574a-3db1-8236-76df706c3b6b | -21.77993 | -52.73896 | 2025-05-15 05:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 337b2a8c-6489-3f9a-b1e8-85c7f72c4a99 | -23.64446 | -54.5677 | 2025-05-15 05:21:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 901f3cca-e254-34f1-b7fe-e904d0e6a247 | -21.05342 | -55.9956 | 2025-05-15 05:21:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e22a1c0f-df8d-331a-82c5-9c273c983f14 | -23.60926 | -48.2922 | 2025-05-15 05:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1961e8df-9113-3069-8523-2cf4813280a5 | -23.60535 | -48.29449 | 2025-05-15 05:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 43267aee-352f-3f8e-af78-218a72653a7e | -23.60165 | -48.29897 | 2025-05-15 05:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 901c3d54-f65e-3bbc-b78e-31058e4e4693 | -21.78251 | -52.74345 | 2025-05-15 05:21:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21a0f0af-0ffa-3ccd-9f57-9d7461cc75ef | -23.60212 | -48.29191 | 2025-05-15 05:21:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c18bb6e4-b3ae-3973-ac67-42a4bd22d1d8 | -5.57199 | -42.92643 | 2025-05-15 05:25:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d2a6d5ef-2df2-3d2b-9b31-fff86eceddf4 | -9.61872 | -40.34277 | 2025-05-15 05:27:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0ad112bf-a0dd-3483-ba39-74763538affd | -11.78074 | -47.35444 | 2025-05-15 05:27:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 58f4c36a-e3c8-329f-94a2-60f0f9ad5c72 | -6.17443 | -48.05139 | 2025-05-15 05:27:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| cc8869a2-1d99-30f6-9b63-db52ce7b7859 | -9.60899 | -40.34139 | 2025-05-15 05:27:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 4fd87840-9612-3785-a967-35b6bf82f3f3 | -11.55454 | -47.61177 | 2025-05-15 05:27:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d3e24744-e53f-33ab-93f8-a33a500db340 | -8.58274 | -45.88538 | 2025-05-15 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e4e14f17-6975-3f09-bfe9-f712fc4e7b66 | -6.65515 | -41.98767 | 2025-05-15 05:27:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 618c71e9-6aeb-3049-b442-6147b5674002 | -6.17176 | -48.06793 | 2025-05-15 05:27:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 316ffcd0-444b-32dc-9eb6-35f8b28712a1 | -8.58444 | -45.87448 | 2025-05-15 05:27:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c2456927-4671-3c04-8965-3d1bb876464b | -11.56033 | -47.44445 | 2025-05-15 05:27:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef08c0af-a9a8-371e-979d-07d516d01431 | -7.94798 | -49.76353 | 2025-05-15 05:27:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7d53167f-5621-39f3-8287-8095a7222def | -11.56232 | -47.43212 | 2025-05-15 05:27:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b5f329a3-bf0e-3382-922a-06a4914316ce | -6.645 | -41.99527 | 2025-05-15 05:27:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 7075c695-3512-3005-87b7-ee6c987c6eb7 | -11.64842 | -48.10551 | 2025-05-15 05:27:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6342f4fa-27b0-3f64-a850-672ecbc9fc17 | -10.33247 | -47.9682 | 2025-05-15 05:27:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ce625387-9d66-3605-b2bd-2a8b4a10bd68 | -7.74271 | -46.33191 | 2025-05-15 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a9d9d814-1188-3082-9df8-7e76d18730ca | -6.64632 | -41.98639 | 2025-05-15 05:27:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| c74afaf9-5432-3ffc-b2a0-308a3df8223e | -15.25853 | -51.4651 | 2025-05-15 05:29:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9df821ea-9cbe-3097-b0b4-a54b4650497e | -13.27595 | -45.4299 | 2025-05-15 05:29:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7cefb2cb-307b-3dae-9baa-85f44bb8f44f | -13.26841 | -45.41903 | 2025-05-15 05:29:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1b73deb7-f5bd-3998-a569-4965b99bcb54 | -13.07257 | -47.80565 | 2025-05-15 05:29:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 93fb2181-0426-35de-9405-16c1c2bca6d8 | -15.25669 | -51.46974 | 2025-05-15 05:29:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9173b276-d7be-3b2c-b4f9-442501dfdce3 | -15.26063 | -51.44836 | 2025-05-15 05:29:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6ab0dcb9-5555-3b86-8dde-7735c9c28eaf | -13.27741 | -45.42047 | 2025-05-15 05:29:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a27e30fc-5b9a-3724-9708-c0b3be703239 | -23.60853 | -48.28903 | 2025-05-15 05:31:00 | AQUA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 04a39083-ba52-31f6-b80d-003ba01ac9bc | -23.59941 | -48.28724 | 2025-05-15 05:31:00 | AQUA_M-M | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 14.5 |
| d031160a-d22f-37d0-9139-99940ea208a4 | -11.0789 | -46.1245 | 2025-05-15 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f9d63763-9238-39cc-a1fa-9fe8ecb674e3 | -11.0789 | -46.1245 | 2025-05-15 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| b2a49fb8-533c-36fd-96d6-2fced9aa6146 | -11.0598 | -46.127 | 2025-05-15 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b1d58d03-0346-352f-9f5b-9904f4844e7a | -11.0792 | -46.1017 | 2025-05-15 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d6e8911a-5ec4-3ce8-a8d3-08fca9d061e3 | -11.0792 | -46.1017 | 2025-05-15 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| ed3a9473-0a62-328f-9c14-38114573eb7c | -11.0789 | -46.1245 | 2025-05-15 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 019e176e-2a70-38fa-bff2-2bccce99490e | -11.0792 | -46.1017 | 2025-05-15 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 513ab988-ae01-3721-bc07-b4bdeb4e9ccc | -11.0789 | -46.1245 | 2025-05-15 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| fb73d48e-e53f-3f7d-92ea-7a0c5f4578e2 | -11.0598 | -46.127 | 2025-05-15 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| fd0828b4-86b6-3ceb-8024-f1532a5d264a | -12.3519 | -49.9617 | 2025-05-15 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 09392da8-4a5e-3f94-9916-2c5065fd90db | -11.0598 | -46.127 | 2025-05-15 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| df3a80f6-b0f5-361d-855a-131d3bb5d86e | -11.0789 | -46.1245 | 2025-05-15 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.0 |
| 90e0d48f-e7c8-3cb7-9342-889d80c573e7 | -12.3519 | -49.9617 | 2025-05-15 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 70a763af-7230-3854-a720-c19d94cc54c5 | -11.0792 | -46.1017 | 2025-05-15 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.9 |
| db1d6a41-dd36-3422-9cb8-c5c60b5b4f64 | -11.0789 | -46.1245 | 2025-05-15 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 6761dc61-0948-3527-a96b-4555320be3cd | -11.0792 | -46.1017 | 2025-05-15 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 9a2bb15d-51bd-310c-91fd-fb9ef0d2e270 | -12.3519 | -49.9617 | 2025-05-15 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 79c78fa6-6b62-3b55-9262-cf042c45e61c | -11.0792 | -46.1017 | 2025-05-15 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| f498cb0d-b01f-396e-b9c1-8cfc5a3fd5ba | -9.6825 | -49.6995 | 2025-05-15 12:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 39071b05-8a72-3a34-871b-c9f0766c62e3 | -11.0789 | -46.1245 | 2025-05-15 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.3 |
| f0eb4d60-62d2-32ae-bfb2-5335ab04f915 | -12.3519 | -49.9617 | 2025-05-15 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f457038e-e577-3dcc-b00e-35077ba6409a | -11.0598 | -46.127 | 2025-05-15 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e3d5e779-6ec2-32ef-a1bd-63847504437e | -6.90137 | -43.74211 | 2025-05-15 12:19:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 248ce3b5-d54c-365f-8140-a29702cad65a | -6.72196 | -47.58993 | 2025-05-15 12:19:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 65a324e9-a502-3f07-af55-5ee4ecc09982 | -10.50747 | -46.17391 | 2025-05-15 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 8d126c0d-9fee-3bba-9440-fd3a50b69b8f | -10.86966 | -44.87357 | 2025-05-15 12:19:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ba0ff470-ecc3-3b76-9953-fe5043a5ab00 | -6.75175 | -44.5349 | 2025-05-15 12:19:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fa10092b-18b6-3b0b-8214-9bbd70171bca | -9.69162 | -49.69688 | 2025-05-15 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8178a74c-aca2-3c2e-bbef-7f940a29fe9a | -7.73616 | -46.32992 | 2025-05-15 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7fc2857-b4a4-3a77-bf66-72feea360bb2 | -7.08763 | -44.37405 | 2025-05-15 12:19:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3aea9d2f-dba2-3d2d-82c8-8b75718ac3e4 | -11.07768 | -46.11989 | 2025-05-15 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 4e02d648-6f8e-3fda-8aff-3231c9caceb2 | -7.32304 | -43.30357 | 2025-05-15 12:19:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| f84a8a8d-8489-3055-a487-5b47c82bc872 | -10.67963 | -47.19695 | 2025-05-15 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b675071b-0512-33c7-a518-027b75c81ea7 | -6.1594 | -44.29081 | 2025-05-15 12:19:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ddbba4b9-2b1c-3db9-a36a-fb474bb978d3 | -8.02186 | -49.62195 | 2025-05-15 12:19:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0041ce0c-2feb-304b-a0c6-afeda17aab81 | -9.68951 | -49.71048 | 2025-05-15 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eacf5bd8-7ea4-321e-aa1b-601ed4cb67b8 | -5.77692 | -43.61387 | 2025-05-15 12:19:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5b36b918-376e-3cf9-9183-bd709e6fcd16 | -9.67874 | -49.70878 | 2025-05-15 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 1ebbfe7a-0a41-3260-b639-c01d0910468b | -5.89112 | -45.06081 | 2025-05-15 12:19:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 2157c34d-af45-3b9a-85a6-47989fd8a494 | -7.74409 | -46.33764 | 2025-05-15 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fe04de09-7d8f-3c9c-98fb-8106f30ed842 | -6.9529 | -42.79725 | 2025-05-15 12:19:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 6c68dba5-62eb-3c94-96f9-e0b55e1e2773 | -6.84396 | -43.30266 | 2025-05-15 12:19:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5c5aca53-3b35-3d57-88d6-2d6bc807badb | -6.17269 | -48.05288 | 2025-05-15 12:19:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9098caee-bb98-31dd-9eb9-011077b8b48c | -10.46491 | -49.91756 | 2025-05-15 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 742f7640-9d72-3970-81cc-ec7a0cccaa92 | -7.20635 | -46.91161 | 2025-05-15 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6bca206c-708b-3cb8-afaf-ca9fc2465595 | -10.87858 | -44.87481 | 2025-05-15 12:19:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46949a3e-befa-35f5-80ef-4e93fc3abf5e | -11.07013 | -46.10961 | 2025-05-15 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 5b96fe40-93cd-35b0-8a60-1b550ef32971 | -7.19852 | -46.90042 | 2025-05-15 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5bfc8032-c74d-3733-ae34-365c729e9f58 | -7.71788 | -44.54253 | 2025-05-15 12:19:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4ad7bd94-07ba-3e5d-bda2-ba36f61c5736 | -8.68653 | -50.01325 | 2025-05-15 12:19:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0b1f6dff-9fdd-39f2-91f1-53f0e3eccf45 | -6.64954 | -41.98605 | 2025-05-15 12:19:00 | TERRA_M-T | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 47c7cba6-91c2-3d09-b128-c973824d2531 | -9.68085 | -49.69522 | 2025-05-15 12:19:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 42d4e55e-9461-39e5-a645-8249f8cd5a7d | -10.46722 | -49.04789 | 2025-05-15 12:19:00 | TERRA_M-T | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0014d8d8-e5d9-38cb-8815-45d6225f15ae | -7.29695 | -43.29023 | 2025-05-15 12:19:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 43eae054-9ce6-3a4e-9777-5b8dad024e30 | -8.12946 | -47.09926 | 2025-05-15 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 43cd9269-e94b-3aaf-bc3b-7587ab4e1ab1 | -6.84528 | -43.29327 | 2025-05-15 12:19:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1a0bd5e5-d752-3f48-bf15-40b5bafefd9e | -7.29828 | -43.28074 | 2025-05-15 12:19:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README14.md)
