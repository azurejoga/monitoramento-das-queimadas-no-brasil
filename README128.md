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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa76475b-d817-32bf-85bb-9922824d8d03 | -2.82623 | -54.09687 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f3d4c2e-984f-3d78-bc4f-bb56af08ab8c | -2.77953 | -51.72232 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50e232f3-7f51-3044-b502-7033def8dd33 | -3.05384 | -54.05054 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b26fbe35-b8c0-3249-83a8-0df507f6befc | -0.05954 | -60.68505 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58848c83-ee6e-36bb-bb49-7b8aaf2d377d | -3.49129 | -53.81767 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cdc35dd6-dc6f-3386-8c80-614e141100d0 | -2.78554 | -51.7196 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6240a0-fe69-3f1a-8564-17f1123c9652 | -1.71394 | -52.6356 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea2fd344-8e1d-30e5-9472-f3b2cc2697c1 | -1.28337 | -51.72987 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c6807e1-39be-36b1-8d4e-a829b78b317a | -3.7918 | -58.97589 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6486a4d6-55ef-3af4-945b-4affc1681d89 | -1.09368 | -53.38816 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8688a02-f756-3300-b1a3-1ad2ccbe6430 | -2.80782 | -53.05332 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a9acbd4-0db4-3ba5-bfb9-0dc5d237f64b | -4.44339 | -48.5678 | 2024-11-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a8eae4d-e9fb-3741-93dd-01220f58aed5 | -1.96608 | -52.89685 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410e4a4e-d28e-3e15-8ad1-714d33609ab5 | -3.35497 | -49.7659 | 2024-11-30 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 770dffc1-fdb7-3c8d-a7b4-9bff757321d8 | -3.52611 | -62.77117 | 2024-11-30 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eef7c80b-4e2d-356a-866f-1ebedef39787 | -3.24046 | -53.9234 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 127e430b-b647-3b9e-a400-e17501a0d85b | -3.63609 | -54.4416 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55814b51-05f4-3cbf-a4e9-68f7c84fea0b | -2.36721 | -56.1175 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039a12c4-fc5d-3fc2-8a87-0f25d530b854 | -1.36334 | -55.18894 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 783ea588-1794-35a9-a914-081133762d78 | -0.90361 | -52.41189 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bff75c5c-6766-3759-bf13-097daa9c91ef | -3.86456 | -50.17201 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e7ce360-3c97-338b-8de5-172c8019daf0 | 0.97783 | -50.25946 | 2024-11-30 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b9aed8-4003-31bf-a9b1-96f636acd9be | -2.04941 | -56.07157 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6504d720-8c8a-3c18-a29c-78f8c44ccc2f | -1.00549 | -51.72634 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9b5dc61f-b0d8-33a9-af80-64a163ffa025 | -3.31434 | -50.03276 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6cdfbe1-4e4f-33f6-919a-b803cb5ec4a8 | -1.05067 | -51.74115 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb16a3d6-dea6-37a9-ab26-bb773b5d20b2 | -1.3106 | -52.86321 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| faa3299e-5593-3188-a211-2d2bfd6e4224 | -1.03643 | -51.73786 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c62c7ad-ea75-30e0-81ac-26f3d8df67e1 | -4.07297 | -50.03281 | 2024-11-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| db032546-36a6-3a94-b9c8-770152d3f0f9 | -1.00016 | -51.72551 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36abdd65-c994-3cd4-91ff-3a5cae4c6877 | -1.36757 | -55.18954 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81b65d55-0ba2-31bf-b509-7c6d137e43bd | -1.32054 | -54.63414 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38a3f54a-9046-3503-8d24-32ab70338f9b | -2.19398 | -53.75161 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e2cd0fa-35bf-3680-abcc-3f220906f645 | -3.14073 | -55.00333 | 2024-11-30 05:27:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc91e46f-0467-3fee-983d-d211770b89d4 | -0.26468 | -51.62125 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c778b390-a597-378b-a72d-5bbc9106bebb | -2.95709 | -51.70069 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d091c7ed-95e9-34fc-9c31-d8d8351588c3 | -1.15377 | -51.69535 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 182cd7a5-5112-3100-b24f-b68d3664ce87 | -3.2123 | -54.17415 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72cfc603-2702-3c3f-8e61-bf3b14d66c02 | -3.6039 | -49.98209 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e034b403-8197-3c32-9d86-650f0a2a21e3 | 1.19179 | -56.00771 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c707cfba-1d3c-3ca0-b567-875f1d8612a9 | -1.70649 | -52.44432 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7019abec-30de-32dc-bc48-e70ea37bcb0f | -1.2484 | -54.54779 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08a13228-c4b0-3496-a36d-72927876c16d | -2.57739 | -55.99516 | 2024-11-30 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f937f278-9846-3075-aaec-88cd81e8588a | -1.61513 | -53.88735 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c2ba9ca-7595-3e64-866f-9edd5304ddea | -2.90702 | -54.18083 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9706b209-739d-32a4-b808-a5cde4e68b47 | -1.29943 | -51.73235 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c188e4b6-79fd-3b46-a612-0ff7a7251bed | -1.62503 | -52.37804 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77abfe3a-efc8-3c8a-9b9d-ce0f1dadeea4 | -1.26857 | -54.56297 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ddf6d24-df55-3ef3-8772-7dc8f90b9bc8 | -1.85206 | -55.61802 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d1b4283-4d51-3202-bb4e-184b8c1106c4 | -1.57887 | -53.85372 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f34c11c6-d551-315b-a4e3-2af4fe23b2d5 | 0.62744 | -60.08538 | 2024-11-30 05:27:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29280c99-b32f-3b92-8f88-135da5743f0a | -3.50403 | -55.40582 | 2024-11-30 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb8046e4-7bbe-31f8-9309-e71855ef2bef | -1.59672 | -52.2852 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 705b8bb2-9a16-3569-b336-ad3614c35bc5 | -3.09298 | -50.35065 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a0f9af84-6a17-3a9a-a39c-8eb0da585557 | -3.33394 | -53.36703 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02c31f00-fdf6-35ae-8f75-8052a2674dfe | -2.97918 | -53.89942 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 377aa734-7846-3377-a5e3-a9afa95821b5 | -1.09868 | -54.1284 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab149585-2183-3f6a-82db-446efdf2e91d | -2.61218 | -54.20765 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f82ef8cf-dcf6-38b2-ad7f-7dafc402b279 | -3.7877 | -58.97924 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 008ba1ec-4c0a-31ed-9257-f3deb0488b95 | -3.30095 | -50.75868 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e6e3344-7d52-3a48-a61a-69bdbd87f892 | -1.53605 | -55.8644 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad4edca0-63d2-33e4-9717-b9a2d9be06d1 | -1.45043 | -52.61398 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7216050-ae07-32d6-ba47-ba61a9100169 | 0.99107 | -50.26937 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aa8fc841-edfa-339f-8fa4-b4cc8d97ac9b | -4.18783 | -54.76282 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aeb6d32-35a1-3949-815a-d7c4929a6534 | -3.26713 | -51.62614 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3dbd417-9324-36e5-bbfc-7d3fcff64ccf | -1.69349 | -52.46101 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca83f58-09dc-3f1c-a813-1c93dfe8e407 | -1.16235 | -53.77917 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0652b21-9779-3c73-94e9-21d1d8790810 | -1.04709 | -51.73954 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fea15ff8-2880-3383-8e44-1b32e0e8acdc | -0.90916 | -52.40971 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26596fa0-0c45-36ce-bd75-603ef66ea53b | -3.14634 | -53.83397 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c7e5c4e-3849-3fa1-b9d8-a7aec7fd2429 | -2.78746 | -52.98527 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bbe7629-0f70-3ea4-ae28-7697f478a837 | -3.31769 | -51.62991 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e082bed-5403-34d5-824a-6490abcd7ae0 | -1.33203 | -52.39045 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfe64f38-2e77-3c4f-a1ec-ca59ac659e6e | -3.10306 | -50.36588 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70aab134-ad67-35af-8c5d-6c9ed78d1f77 | -0.26213 | -51.49836 | 2024-11-30 05:27:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051d1c80-3390-373c-9916-d6826fe812c5 | -3.2979 | -53.83378 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fab6d503-e956-36ff-9ebc-518c8f151996 | -2.78606 | -51.71605 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c56406ff-3161-3926-bc8c-2d2527b35091 | 0.07048 | -51.49393 | 2024-11-30 05:27:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97c0250b-5116-3a65-bbd0-f02c535278d7 | -3.25072 | -51.34752 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e253d4bd-f512-3b21-b48a-8b2eba566cc5 | -2.6949 | -52.9157 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 428d33de-84de-326f-ae76-f5057bff6914 | -1.07697 | -53.63006 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7365e4b0-faf0-3e33-b6eb-85156d796611 | -2.32822 | -50.67558 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba430648-f1ed-3361-81cb-cbaade0f5fdf | -2.8047 | -51.58968 | 2024-11-30 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2febd13-1414-3fb1-824b-a4c032d2db45 | -1.00067 | -51.72221 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23f22572-72d6-3648-bc70-b9bbc634f2d8 | -2.80282 | -53.05254 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90f3a201-c4e3-3b14-9b99-575e98375781 | -3.74499 | -53.39294 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 592d6f9b-db84-3697-9ad6-b9d5903badb5 | -3.7883 | -58.97536 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98c06f2d-a636-33a1-bbb9-a34f49038fb1 | -1.44209 | -55.12849 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d13f7b15-8cd2-35b7-a360-32d561b8a146 | -1.49162 | -54.45576 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ef49f49-30c1-3c00-9818-5e28179a17bc | -1.0723 | -53.62928 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 44e031aa-0b5c-31a5-b72f-325cf6d40921 | -4.18973 | -50.68562 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8efca9ca-35d7-3d79-b40f-3eee12d61e02 | -1.58039 | -53.84413 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15e6b5d4-54e3-3d97-89d5-817197a82933 | -1.70136 | -52.44354 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2263c6cd-7ecf-3b6c-8549-192b49ed294d | -1.08087 | -53.63594 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0815cae-ab6b-38bd-8e87-731534988977 | -1.70884 | -52.76924 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80090e5c-c3d6-3d25-bfb7-503e79275852 | -2.8436 | -54.03199 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0ce558e-e1c0-3cbf-840a-9d0368265a06 | 0.94222 | -50.75201 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d502ef0c-7dd1-37d5-bb21-05157c97c9b6 | -3.28377 | -50.6298 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16c17345-644c-35cc-a153-4b66e070fd07 | -3.31504 | -50.03328 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be1b724e-9f53-3a1a-8b8b-be8fa995fa2e | -1.61599 | -53.62877 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README129.md)
