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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c93417d-3c87-3b74-81a6-b8b251ccbbb3 | -21.31848 | -49.46807 | 2025-05-24 00:52:00 | TERRA_M-M | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| fef2acea-c40c-3296-a888-8996548f03fe | -23.17026 | -50.17723 | 2025-05-24 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 61d1e6b2-2dc4-3e1e-941f-57449c6e19b4 | -20.44149 | -46.37721 | 2025-05-24 00:54:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 2daaf739-8ace-30c0-9820-7ef35d4814a1 | -11.42224 | -54.30835 | 2025-05-24 00:54:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8905dfd2-b17c-3e98-a64a-b2dfbbaa0487 | -11.74962 | -54.22871 | 2025-05-24 00:54:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| fa12eb7f-21cd-3313-a313-a486e2a85a4e | -10.95274 | -48.15692 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 9752ef3e-a6bd-3cf2-b283-009b271b96ef | -12.38803 | -49.99002 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a60635e7-9c88-3a4f-b30b-810afa4d36df | -13.47038 | -52.28086 | 2025-05-24 00:54:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 102e533a-67cc-3cd2-807f-8e216671e1fc | -14.03357 | -55.13492 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 26faeb3a-2606-3b01-86c1-d3b8f98611cb | -12.07144 | -47.35805 | 2025-05-24 00:54:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 159ef2ac-83a0-3019-93ce-6f84f46c0e93 | -20.27563 | -50.74452 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 04bf58ac-0329-3766-9444-be166f354b64 | -11.35747 | -55.13742 | 2025-05-24 00:54:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f7900a2-616a-3f4a-bbb6-46a5d4740627 | -11.76082 | -54.23855 | 2025-05-24 00:54:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6f6312e5-b4b4-36a3-a497-f47583eaa694 | -12.37904 | -49.99137 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 992d663c-fca7-381a-a3c2-b7094fa268e4 | -10.36263 | -47.97396 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0f6a0a14-7e8b-39dc-823e-56fc89c41859 | -10.3736 | -47.99078 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56cca896-3450-30b1-9361-37f072995402 | -11.75106 | -54.2398 | 2025-05-24 00:54:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ae3708f-1917-365e-826f-8101aba65b9d | -11.98995 | -57.22101 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| a4b45dfa-560f-3031-ab99-8fa18a78224b | -12.09183 | -57.38308 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7bb35125-a0e6-397b-9925-7848c62a7e81 | -11.80308 | -57.36113 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 1d7aa6a5-1e71-32f6-9e10-c0bedd5b7238 | -12.36066 | -49.9272 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 43b293ae-53c1-3838-8f0f-2f5b12d44a8f | -20.9405 | -56.58239 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 24f639b6-3b3b-32c9-bdbb-d0651b29bfba | -20.93847 | -56.60039 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 17b64e8f-46e9-35dc-baa1-e83895c7c446 | -20.43969 | -46.36562 | 2025-05-24 00:54:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 521c355c-9b69-3dcd-b007-f8ba2b4cb45a | -20.94289 | -56.6055 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e45dbb05-67f6-352a-a402-bbc73f2a6547 | -13.36617 | -54.25994 | 2025-05-24 00:54:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 5723fb0b-56f1-3fd0-a277-d11f393478c2 | -17.15585 | -54.00294 | 2025-05-24 00:54:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 76767210-da39-3eb9-8131-e4919f79b156 | -20.94963 | -56.57605 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 36.0 |
| cb1e67a8-c309-336f-a9bf-7dcbee8adaec | -13.99023 | -56.01879 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| b396f21d-e4d0-3e9f-82a6-dba9b2ca551c | -19.87503 | -54.36187 | 2025-05-24 00:54:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 76869377-1e42-3dae-a2f4-d33f7a6b98c8 | -10.36336 | -47.99234 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 44710db1-336f-3855-a42d-ac46e1c9f86c | -10.94203 | -48.15279 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3bd8fa7c-88a8-387e-a2ca-463f6c9e4d7a | -10.33788 | -46.65708 | 2025-05-24 00:54:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 826b6502-4651-3783-a38c-c79b4d967c57 | -13.86358 | -59.73253 | 2025-05-24 00:54:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 0877081a-d969-3fa9-b6f8-16f2253f3408 | -19.8776 | -54.37055 | 2025-05-24 00:54:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| aa279f43-509b-3854-a62a-45b33af3d87f | -14.03521 | -55.14862 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3a560d8c-e61a-338e-93b9-b4cd73538eab | -13.18988 | -53.58772 | 2025-05-24 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f158b0dd-5775-37a1-b3c3-4dc3c312fd72 | -20.93626 | -56.57725 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d032a16c-b7f2-3c9f-a8e1-bbbd793bf99e | -14.06567 | -57.11169 | 2025-05-24 00:54:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 513da381-bfeb-3f87-b203-bafc9eb5d56c | -13.18853 | -53.57711 | 2025-05-24 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 7977b3df-10e4-3692-aaa8-cbf776c22cc9 | -13.14612 | -56.81235 | 2025-05-24 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| e60d9085-9ee0-3b9a-a761-ab744d39a7cb | -10.36442 | -47.9861 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| d2518ba6-3697-3f7d-84a8-64b3631fa283 | -12.38669 | -49.98069 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7186899f-da3c-3007-b001-83d78a59ee7b | -20.45121 | -46.3754 | 2025-05-24 00:54:00 | TERRA_M-M | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 20.3 |
| bd4c9037-ddb0-3746-9c76-40f94965cdee | -12.3777 | -49.98203 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1af92bdd-242e-3de7-97e6-663c03d2865c | -21.5988 | -56.05458 | 2025-05-24 00:54:00 | TERRA_M-M | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| df6d065e-4efb-3db6-a7f6-81cd360f2124 | -13.79045 | -54.31024 | 2025-05-24 00:54:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 33b3efb9-d0d3-3c09-b824-d3ec9aea7742 | -10.37175 | -47.97871 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1fff936d-736f-3042-adbd-7e2f97a10431 | -10.74411 | -49.28576 | 2025-05-24 00:54:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ffdd3ae8-4612-3467-b779-34e73891e0c1 | -11.56439 | -47.4509 | 2025-05-24 00:54:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a57df9ac-ac9b-373b-bd7d-57ec2ff3e7d1 | -11.75937 | -54.22743 | 2025-05-24 00:54:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c3160e01-3b3f-32a7-9119-bbf16b2e3725 | -14.02285 | -55.13635 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f790383b-9e92-3e52-a6fb-83f14e8790cf | -14.67853 | -52.43793 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 00aeb8f2-746c-35d6-8002-858d386c002c | -12.14084 | -54.65245 | 2025-05-24 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d4b0becd-1907-33dc-9ef3-ccaf526f9b6b | -13.14817 | -56.82998 | 2025-05-24 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1a8aeef3-1b8c-31bf-adbc-4fbaea553c97 | -10.36149 | -47.98022 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 84738a7a-bc11-36e9-b599-97d6b79c3006 | -12.14232 | -54.66422 | 2025-05-24 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ad179f90-b79e-3f95-a19c-b248f67231eb | -10.94117 | -48.75377 | 2025-05-24 00:54:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 134f7bd2-1283-3581-b818-8e340fb32d39 | -12.40467 | -49.97795 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 213b2c2a-ef76-3714-91f8-2fadf151711b | -13.16026 | -56.82845 | 2025-05-24 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 995c51f6-8756-39b9-a41a-5432064aba45 | -12.39568 | -49.97934 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| d0206a32-744a-3146-b6ec-c6175de0c62e | -12.18226 | -54.25315 | 2025-05-24 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4e6e28bb-b876-387b-b327-6dd2f068c7fd | -11.56637 | -47.4641 | 2025-05-24 00:54:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 92816cc1-98e3-3593-bed4-36860f904284 | -10.46919 | -47.9449 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b3bd5a80-ad1c-304c-9016-061fac4c4f00 | -12.406 | -49.9873 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a1f68d51-ba04-382e-a78d-ae18f0385586 | -12.83551 | -47.39124 | 2025-05-24 00:54:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bb3bc852-62d7-3559-a285-f845a7ced67e | -13.15819 | -56.81084 | 2025-05-24 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b0c55caf-f10b-346d-abbd-ad744b5210a8 | -11.81545 | -57.35964 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0006e6da-5e6a-37e6-b72a-a11c9ab9432d | -20.27691 | -50.75425 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fdf16f43-be3f-30ec-8ea8-5500790a1799 | -20.95184 | -56.59881 | 2025-05-24 00:54:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1be59b1d-2831-33e1-8f45-6b7f5afe612f | -12.35301 | -49.93798 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f5ad87f2-e914-30b9-b876-ff9b5c42ff91 | -17.27209 | -48.62348 | 2025-05-24 00:54:00 | TERRA_M-M | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c71bcbbb-3b01-31a5-bd8f-ce68a0323cec | -21.59797 | -56.03828 | 2025-05-24 00:54:00 | TERRA_M-M | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7c20158f-7049-3234-8d3d-69941e401f82 | -11.99354 | -57.2142 | 2025-05-24 00:54:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| b64cb0f7-3e7c-39b4-8148-df03c9eeb4ed | -13.36764 | -54.27171 | 2025-05-24 00:54:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ca23ff0c-947e-3e0f-9741-eb5840bf6ae8 | -12.39701 | -49.98868 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9d0a4245-ca66-3552-ac6f-63fa1f063feb | -12.35166 | -49.92858 | 2025-05-24 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0e243684-cfef-3147-82fb-a5f1f334dc0c | -10.6546 | -49.4771 | 2025-05-24 00:54:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72c06fe7-9789-322f-8ff6-6da361a073fc | -12.06947 | -47.34524 | 2025-05-24 00:54:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| dd753583-e911-31d8-a96c-7fa434644026 | -10.95093 | -48.14512 | 2025-05-24 00:54:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f2a5ef69-90f4-3c76-abfc-feac02bebf25 | -10.33712 | -46.64822 | 2025-05-24 00:54:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eddc91e4-270f-3db1-b2b8-246ff341ff2d | -9.72969 | -45.43049 | 2025-05-24 00:56:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a68a7511-8966-3afa-8f3e-c3b925c5584b | -10.09333 | -47.08432 | 2025-05-24 00:56:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a916b936-dee0-39f1-962e-ac7091ccf550 | -10.53147 | -55.71783 | 2025-05-24 00:56:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8b32cd34-d4c3-35d6-9f4e-64b18204035c | -9.11075 | -47.65078 | 2025-05-24 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 484637d1-6dd9-3488-9e5f-27e266ea654b | -9.96541 | -49.81314 | 2025-05-24 00:56:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dbadb0e8-f377-3673-b754-73d152367988 | -10.60063 | -52.84381 | 2025-05-24 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eabe04d2-e1ee-3b19-97d5-daa67e68a59f | -8.75172 | -48.03354 | 2025-05-24 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9c520311-2fee-3369-bca5-e17ab3b10ebf | -10.37131 | -57.50464 | 2025-05-24 00:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e5c873eb-ee8e-3140-946d-49c41acd2f6b | -6.23048 | -43.38203 | 2025-05-24 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 761f13a0-080b-38d8-93c1-055f94762197 | -9.07758 | -49.6768 | 2025-05-24 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a2edd0ee-478a-36df-a9ca-b5eec119d63b | -10.36541 | -57.49376 | 2025-05-24 00:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 7869d291-759e-33e8-a1dc-0019bdf62739 | -10.02986 | -48.69789 | 2025-05-24 00:56:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1fb60cd5-c5dd-36cc-bdf4-adce31ed6dbb | -8.75366 | -48.04638 | 2025-05-24 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dce94a0a-17f8-3156-9d2f-897e28f51090 | -6.22509 | -43.34922 | 2025-05-24 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 921278b8-b425-3f81-a79e-44caf9f8c866 | -8.08342 | -43.1164 | 2025-05-24 00:56:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 56f88999-059b-3a40-8672-dbe81ab0221f | -6.21619 | -43.35598 | 2025-05-24 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ba7c951d-719a-313b-a8ba-de07456293c5 | -8.06783 | -43.11922 | 2025-05-24 00:56:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| d0bd06da-d5c5-39a5-9990-754cf02b56c2 | -6.23207 | -43.35345 | 2025-05-24 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 932b5d4c-6f96-3b03-bccd-0b41e67609b0 | -9.11815 | -47.65543 | 2025-05-24 00:56:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README4.md)
