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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40702fbf-e83d-3462-a0ff-7497bcc95ca0 | -14.63529 | -48.14153 | 2025-07-07 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18533c53-7d40-315f-8939-159d53374b03 | -11.87936 | -58.72776 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d21a148-138f-3ff6-879a-e3598d6cbfe3 | -13.64707 | -46.81298 | 2025-07-07 05:01:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61bd7a6a-e818-3c7b-b7e5-b9d9ab21a15c | -14.127 | -51.30303 | 2025-07-07 05:01:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 2c5148cc-ba9f-3cfc-ae3a-d1f15e501ac0 | -12.57732 | -56.96923 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22cb4208-2d7c-3604-95d3-8b7df51d4e47 | -13.01564 | -46.76447 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d6b612d-090a-31f0-9ddc-b4794cb121f3 | -13.01983 | -46.77385 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a2ee7fc-6b41-33dd-b834-e00eb0e9e508 | -17.1709 | -42.83929 | 2025-07-07 05:01:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08d78155-5e86-398d-865a-2832180548a7 | -13.01529 | -46.7673 | 2025-07-07 05:01:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ffe7e94-2f6d-3c75-a980-59f56b8cba87 | -14.63209 | -48.14751 | 2025-07-07 05:01:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0811eb44-bf37-324f-8030-05563612ebf0 | -15.74503 | -47.78318 | 2025-07-07 05:01:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9c23191-7859-3b83-8efa-e2808ff90175 | -12.74967 | -44.41592 | 2025-07-07 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27bd2a72-7d13-3e59-b91d-729e9771dfac | -16.27081 | -47.57171 | 2025-07-07 05:01:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0cb67d6-a2ed-3698-9165-fc6d5d71bd94 | -12.02453 | -57.07801 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 423d7425-0cce-35f0-9fcf-6656bf6d3bb8 | -12.75521 | -44.41517 | 2025-07-07 05:01:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83bda3da-886e-34c0-b026-5099c4bbc3bd | -15.07756 | -48.94656 | 2025-07-07 05:01:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3f682a9-3610-3cb6-ba00-e9c623cfd094 | -12.02732 | -57.08228 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ece0ad11-bbc2-3117-b1c5-84d7ade4dd7e | -12.02792 | -57.07858 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8245a290-40b9-3381-888c-773b17c97140 | -11.32763 | -55.21542 | 2025-07-07 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8ea7dda-ef0a-3dee-9f25-27d8755fafd8 | -12.02332 | -57.08541 | 2025-07-07 05:01:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cf68301-e8f9-3a0d-a3e8-5fa155b81caa | -11.87864 | -58.73206 | 2025-07-07 05:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f0db2ef-a63d-3923-8e26-a119c4a50dd0 | -12.5795 | -56.97711 | 2025-07-07 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 197b965f-68f3-3a16-9303-072a126b926c | -24.7434 | -53.80822 | 2025-07-07 05:04:00 | NPP-375D | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 34092fcb-8d48-3b27-9585-30fd24844826 | -21.97131 | -57.58571 | 2025-07-07 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e643b29d-43a8-3c3e-a1ba-7aab805c20e2 | -23.98073 | -48.91903 | 2025-07-07 05:04:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08789c1e-2d89-3564-8ad4-33f2bb9ffb22 | -21.02677 | -53.92344 | 2025-07-07 05:04:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f1f3a8a-90db-35b9-b7e6-fab0b7adbbb2 | -20.47699 | -53.67521 | 2025-07-07 05:04:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f463316-143d-333c-915e-ca9fd54df04e | -23.9814 | -48.91981 | 2025-07-07 05:04:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c7f7ac9-7935-3912-8077-84950d035781 | -20.63038 | -55.33369 | 2025-07-07 05:04:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07f6ff7-da29-38c4-b616-bfe31a6646a8 | -26.69147 | -53.52128 | 2025-07-07 05:06:00 | NPP-375D | SÃO MIGUEL DO OESTE | SANTA CATARINA | Brasil | 4217204 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74dd229d-0ce4-36d6-b2c5-9ef2df392268 | -26.69086 | -53.51975 | 2025-07-07 05:06:00 | NPP-375D | SÃO MIGUEL DO OESTE | SANTA CATARINA | Brasil | 4217204 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b6b27324-9029-367a-9ab3-08ca94fad091 | -6.1791 | -48.0712 | 2025-07-07 05:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c10455b9-4401-3b7e-860d-8699734cf518 | -6.1792 | -48.0494 | 2025-07-07 05:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9b5f76b6-d77f-33de-86d0-7168f11b049e | -6.1792 | -48.0494 | 2025-07-07 05:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 0e1391ab-da1a-3fd1-8295-642dca3e6950 | -14.1324 | -51.3017 | 2025-07-07 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4d81dd8e-651d-3b15-9edf-09f766387984 | -6.1606 | -48.0507 | 2025-07-07 05:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 275341c3-6254-3861-abbc-2afc643c51de | 0.69165 | -51.45935 | 2025-07-07 05:21:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf01c167-3434-39c7-98f2-055281d62426 | -6.70493 | -47.79847 | 2025-07-07 05:23:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 3e760cb3-6057-37b9-afff-d16b9929bf19 | -15.07525 | -48.94353 | 2025-07-07 05:23:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cccc9f5-bc11-3013-a738-944b51a0140d | -7.26695 | -44.60707 | 2025-07-07 05:23:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 79952f6a-db08-3422-b836-15d573cb31c6 | -11.87581 | -58.74035 | 2025-07-07 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9a02a25-d73e-3a1c-8d66-204640d8f3aa | -12.02904 | -57.08485 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7d19059-3313-3dcc-aefa-b8b0d34c9614 | -7.26495 | -44.61959 | 2025-07-07 05:23:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c9b2493-6641-3d7e-90d4-f8ab07b5d648 | -2.58494 | -51.92154 | 2025-07-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 254ed7b9-5bf4-3b3b-a90b-f0ec1da0a4f3 | -6.16439 | -48.05827 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d7fd2e9a-637a-3a49-8f76-0c391a1550f4 | -7.69237 | -44.57419 | 2025-07-07 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7cad1254-776d-3a42-a0f7-a2152bd8ad12 | -14.12483 | -51.30634 | 2025-07-07 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37e14287-5553-3ef2-9511-9e1087cac729 | -6.16239 | -48.05305 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 92fc5a45-38cf-3d29-b310-787eaba0b61f | -7.53722 | -61.34798 | 2025-07-07 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f838c1a1-4421-3c67-8185-ea98f25eead7 | -6.17017 | -48.06534 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 1afb90f2-2254-3338-ac8f-46b48ca12d30 | -12.02506 | -57.08426 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0b6435c-0552-3c49-8630-7b99694a6f9b | -6.16928 | -48.04133 | 2025-07-07 05:23:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| b1f923cc-3afe-3bf9-9e38-99a4ecb67666 | -12.02181 | -57.07846 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c290a5d-e028-343a-ae8b-b03008b40e92 | -10.64395 | -44.48497 | 2025-07-07 05:23:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5abf8bf0-fa33-3c6c-85cf-d8553d609f17 | -6.7077 | -47.8039 | 2025-07-07 05:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0be58695-8c4c-3c9d-bd38-b6fdba3bd7dd | -14.12222 | -51.30734 | 2025-07-07 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b093394-d2f4-3ae9-a087-5715b24e5fae | -14.12533 | -51.30177 | 2025-07-07 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ade25f-0db1-3228-9fb1-4bd6e9f29482 | -6.16167 | -48.05848 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8ec7dd16-a6fd-3bb7-8146-4e08f1ee4625 | -6.70688 | -47.8099 | 2025-07-07 05:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 13d318f4-d12f-317b-b00c-c9ede09c1892 | -12.57605 | -56.97102 | 2025-07-07 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ca1108e-8701-3269-aafe-cbbc2b78a92b | -6.17574 | -48.0545 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 02ec16b7-b1a0-38a4-90b1-f2c63fe1df80 | -6.17098 | -48.05954 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0e9c8912-e6cb-333c-9d41-9875bb7676ac | -12.02976 | -57.07961 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ca589ea4-dc9c-3c7c-a0fb-fb8949490a44 | -12.58009 | -56.97159 | 2025-07-07 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad12757a-bfe5-3390-a620-0ada1d61537b | -6.71022 | -47.80006 | 2025-07-07 05:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 184f223c-fc3a-3306-81fd-64c72ffeee37 | -12.02652 | -57.07376 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bd66d64e-dd73-3376-9009-6f072445eea7 | -12.57959 | -56.97522 | 2025-07-07 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89e9cc3-ae87-33be-889a-395186e67bf4 | -8.05763 | -43.112 | 2025-07-07 05:23:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| bed43a2f-e2d7-3df3-b1e0-c0e4a9da088b | -6.16518 | -48.0526 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f164ee33-86ec-340a-ba72-ba68e0520481 | -6.16905 | -48.05389 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1014a466-cadf-3560-aa4f-4678bf53eb88 | -11.87763 | -58.72774 | 2025-07-07 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cc374af-5921-3511-9af2-5460d723f0ed | -6.16826 | -48.05981 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 88f02891-dbf7-3ed2-8058-b9b1565c9bea | -11.88063 | -58.73254 | 2025-07-07 05:23:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 916069f3-a93a-3eb5-9014-c73ccfa9aada | -7.69576 | -44.56889 | 2025-07-07 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d956ea7c-d873-358c-b362-98bc523aebda | -14.12275 | -51.3028 | 2025-07-07 05:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f95b504c-91df-37ed-9c78-79345de4bcbc | -6.17487 | -48.06096 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e9fa731-f5bd-3351-9739-26d28fa269d5 | -6.69962 | -47.79009 | 2025-07-07 05:23:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| aa5e0f59-80c5-300d-909d-8515b972374d | -8.05604 | -43.12214 | 2025-07-07 05:23:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3aa6c537-4a04-37dc-b067-773679bf2397 | -6.70942 | -47.8062 | 2025-07-07 05:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 375a001b-f84e-3024-8baf-9f3ad9edacac | -7.90575 | -61.51022 | 2025-07-07 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee8cd6a-0a64-34ce-9e48-17c3af3ef0a2 | -12.57909 | -56.97884 | 2025-07-07 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2885f0-ac2d-3b47-aafc-c0a3c04fd19e | -12.02579 | -57.07904 | 2025-07-07 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83b00c0d-2cbf-33d9-9896-a4c82b5dc7de | -6.17185 | -48.05333 | 2025-07-07 05:23:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ded70a6c-8615-34b5-94f0-21f60c8c7ba5 | -2.58779 | -51.92196 | 2025-07-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5382cda-9f00-321b-8bca-eb5be774fe53 | -14.93162 | -55.83679 | 2025-07-07 05:23:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d64d4ebe-2f31-3284-883b-d2b79662e79e | -6.16527 | -48.06573 | 2025-07-07 05:23:00 | AQUA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 13242f95-b0a9-3b77-b368-5aca298c23f8 | -7.68342 | -44.57988 | 2025-07-07 05:23:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f3c95c1b-8934-396f-9f80-e5d4b7d49db9 | -9.58067 | -57.39643 | 2025-07-07 05:25:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0b72d401-9353-3eb0-9ef4-7fede98feb78 | -11.32288 | -51.44528 | 2025-07-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f521fca0-62cd-374e-83b9-e80954ad0a44 | -10.57564 | -49.13185 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6cb27b2-ffa1-349d-b44f-a79023945c59 | -20.63055 | -55.33368 | 2025-07-07 05:25:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09fbb2d8-d0d6-374f-a9a7-0a4207fb795a | -9.93129 | -59.93867 | 2025-07-07 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66ec00fc-8082-34c1-8b9b-4cb4b4c4cb84 | -11.3286 | -55.21582 | 2025-07-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 193aaee2-393c-368e-b9dc-e69d7d82e335 | -10.56766 | -49.1331 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b41b06fa-e5db-3b08-bb7f-4b98ac091ee5 | -11.33439 | -51.44674 | 2025-07-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f03c3a84-799e-32b8-8565-e97e99ff1c65 | -10.57699 | -49.12096 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d03211b-a051-3795-a013-c166f61b3019 | -11.33301 | -51.447 | 2025-07-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6493174b-1a6a-3fce-8a91-36e259f695c8 | -10.57423 | -49.13402 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df8e175a-f6db-316b-b27b-6c480d4bacbc | -10.56839 | -49.13644 | 2025-07-07 05:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87661269-f187-3dec-aee8-f7e0f90aec86 | -10.13113 | -57.77909 | 2025-07-07 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
