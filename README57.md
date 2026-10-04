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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2b6fb63-60e9-39de-ae99-c4353f431a69 | -2.97004 | -54.09557 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8868e8da-fe6a-315a-bdf1-0f24699af5b8 | -4.11474 | -54.41474 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96e1216d-f647-303d-ab67-1483699bb513 | -3.79039 | -59.37544 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77708650-5d16-323e-a642-fef362b9d12e | -3.01352 | -53.88501 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a91141a-abd5-308e-b141-e6729abdfd13 | -2.97476 | -53.26225 | 2026-10-04 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b23c736-0ca8-3ae6-8221-cb070f666225 | -0.36034 | -51.98471 | 2026-10-04 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc540a2d-2bbd-3d03-a828-60b3d9ebe934 | -3.12766 | -53.75127 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21aa04f0-af80-378f-8d4a-81d188e9f404 | -2.59283 | -51.85347 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e9974061-d5c9-3eb9-af4a-3aa49c3aa2c1 | -3.88974 | -49.69683 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 30ace026-9459-3792-9253-1fccb6192a8b | -2.81873 | -54.13821 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e859879-506f-3a28-a651-76dfd7bc6f32 | -2.53547 | -58.03709 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4b6e50b-321e-3f90-bc15-1e9c73b2f7c9 | -3.13251 | -53.7436 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 393ff798-930c-37cd-af6b-14419ec7c973 | -3.89911 | -49.69861 | 2026-10-04 05:16:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9979ba8f-80ab-3d20-a383-729edb3da7c1 | -3.20616 | -50.75098 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7e932a17-3209-346f-9986-5de19460c094 | -3.79325 | -59.37985 | 2026-10-04 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84b258b0-3de9-3325-9a0d-90cc894bb8cf | -3.17996 | -50.53862 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1caefe7c-c0d2-3601-a90e-dd01a3bca180 | -3.00546 | -53.87209 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c98aab60-f91b-3e92-a3da-de8d8725f166 | -3.16801 | -54.07985 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a644f7d6-7fbb-3fcc-b38c-5e546e557dcf | -3.18394 | -54.09383 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 062d5ba0-6946-3646-b5aa-76c2d572bfd0 | -1.33027 | -54.6648 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 98c1df6d-8f50-30b5-ac43-0d8eaabf64e7 | -4.27654 | -50.27671 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a40c4e7a-bc44-35b0-a365-21335669a955 | -2.81248 | -54.10917 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9fc1c4c4-f996-3fe3-8c78-b5c06e7104dd | -3.169 | -48.5853 | 2026-10-04 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 019d36f3-e8dc-3e63-9717-0eed23fa0ea3 | -3.1127 | -53.74185 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| e8852b5d-1f22-3779-8cda-e6309075b02c | -3.8665 | -55.81044 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e39588c9-e63d-3c16-b94b-fb6084a1bd4a | -4.2909 | -50.27408 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 62cc324f-c58a-3231-8423-f97c96138867 | -4.28495 | -50.28264 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8660ec6f-b1f2-392d-8c6a-c48f082f8d75 | -3.04706 | -54.22753 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 27d537cc-2db5-3a29-a774-fe06d351118d | -3.11823 | -53.73006 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75956828-74c5-3964-a437-ab302771506f | -2.80728 | -54.0963 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45cac9fc-70d0-3ba2-b7d6-851ceac96f71 | -4.26332 | -50.74929 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1751970-beff-3816-af3d-ce0979638612 | -3.11694 | -53.7383 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbcec15f-57b6-3ae2-8b2a-907f2b476213 | -2.77064 | -57.00508 | 2026-10-04 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad71511c-e48d-31e3-be5b-0e11f5986a88 | -1.26319 | -54.55732 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30bd85f9-33aa-35a7-94f1-e01ed372e996 | -4.12941 | -54.15716 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7891efb-182d-3fa7-b521-c076409bb493 | -2.89921 | -54.13305 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04dfdd4b-2505-3faf-bf90-ba8be128c9fd | -2.81309 | -54.10524 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2daab519-eb5d-33f2-a4d0-db58426c2144 | -5.86315 | -55.7047 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fab40400-8f1d-365f-ad3e-0adfaa8428bb | -3.70537 | -50.66193 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fe95395-c4a5-3d71-ae20-e4ee6206eeec | -3.85087 | -55.80075 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9253571a-1e73-38db-9c07-9dcffae7fce8 | -1.10243 | -54.11339 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02f4f657-1c92-377e-829d-4730fca05211 | -3.18446 | -57.86353 | 2026-10-04 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc5881b-79b6-3600-be23-cf4531735de2 | -2.98039 | -54.10062 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7eb5392-c6d5-3881-937e-ee61c41dc86b | -1.26588 | -54.56426 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c3285fc-0616-363a-8e0b-4c8b45716b6d | -3.90842 | -55.88565 | 2026-10-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67ddf7ef-e49f-34d7-b890-b7c9adf371e7 | -3.56728 | -51.98528 | 2026-10-04 05:16:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccfb2e8d-d4e7-308e-8f42-ae3d277e70b3 | -2.95035 | -54.12878 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 89e4766d-612e-3f17-ad10-c34797e3eba9 | -2.91943 | -54.09586 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3cd8074-cbad-3f08-9568-dc6cdfa3c092 | -2.79258 | -54.09805 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29b0efa0-8b02-36a9-985f-0807088d021d | -5.82653 | -53.50271 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1627cee-7dcc-340e-a1e3-bebd3f078061 | -1.09551 | -54.1123 | 2026-10-04 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4ff81e76-ba9e-3fd8-8720-6f4cc5c0ac68 | -1.31883 | -55.91634 | 2026-10-04 05:16:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4dd5a2d-8904-3a4a-927b-bd613c2179d1 | -3.09692 | -51.10022 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb81f83b-45b7-3da2-aa58-087ea11a49fe | -4.28109 | -50.27743 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 930032ba-c95d-3873-bdeb-b1b8bb5822e6 | -2.80712 | -54.12041 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55643704-554a-3562-9b21-5c9cbd90f360 | -2.93632 | -54.19486 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2753414b-5023-350c-8a50-59d2d398b9f0 | -3.07436 | -51.28078 | 2026-10-04 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eab1bceb-228e-3b39-ad47-61969a03ae13 | -2.96628 | -54.09845 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09707fa6-7ad6-3c71-bbb8-6eb33b33945e | -3.2137 | -53.94669 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a961714-2690-3daf-a64b-f18194a752db | -2.93977 | -51.27648 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62848025-1b45-323f-870d-d6678a23e995 | -2.88417 | -54.09043 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b93481ef-35c3-3b17-894b-03581a7341cd | -3.46406 | -50.09859 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c79d375-855e-3077-ac42-a5d1e06d9169 | -3.04375 | -54.20297 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 473bd86d-9060-39d0-b57b-4de223858214 | -2.47831 | -50.87854 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b5d62b2-a0ff-3c77-a0c2-7ef8938678c0 | -3.13296 | -53.75336 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2dafc93-efcb-3859-8278-3f20ca342a12 | -2.89035 | -54.1437 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4ba588-b486-34cd-9c76-865d39e629c6 | -3.4646 | -50.09983 | 2026-10-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec5de560-7f6d-327b-9f6d-71c1f6be4684 | -6.01552 | -53.53247 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c7047e-a126-3f7e-a141-edee4445add5 | -5.22635 | -48.40931 | 2026-10-04 05:16:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ef81a2e-0acf-33aa-8a18-73c7777d43a6 | -2.58884 | -51.85289 | 2026-10-04 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3fe67610-df82-345d-ae0e-719280d377c6 | -2.15523 | -53.6628 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1632bccc-4f32-311a-964e-50b46f2cfb5f | -3.51236 | -54.60718 | 2026-10-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 450c8d9e-f087-3d53-94d9-75f0abba07c4 | -3.97597 | -59.34176 | 2026-10-04 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8034f27-2f95-31f0-813b-e6ea96ae9889 | -3.76246 | -49.5668 | 2026-10-04 05:16:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0962adde-69fd-3bc3-988b-f959c1d6698d | -3.12348 | -53.7435 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102859ca-97d4-356c-a40f-d63e3cec82d3 | -3.12892 | -53.74305 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cc968da-bae4-3b4d-8918-af9e8e21c4be | -3.13391 | -53.72404 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54d8d257-3eda-389e-ab1e-c8942496ec10 | 1.04044 | -59.46317 | 2026-10-04 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24e58f83-03d5-3a7a-8d58-c33b1a48334f | -3.86152 | -55.97215 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb8cc282-92ff-3945-a955-75d3791dd2dd | -3.86371 | -55.82812 | 2026-10-04 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1812944-9dc8-346b-9683-2e5b936f46fc | -2.21668 | -51.95535 | 2026-10-04 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c86050c-9e09-3814-af3a-66d4d1519c94 | -4.53987 | -55.97253 | 2026-10-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83f4bc15-6554-373d-bd60-2b9c470eb6b0 | -3.18155 | -54.08593 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 510f5454-b124-36ff-91e5-a4b80c87c2c6 | -4.14852 | -49.6967 | 2026-10-04 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fd33b31e-863e-3223-bedd-3a0fe06a2945 | -3.13196 | -53.73637 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63841895-787e-39f9-901e-b4bff34abd64 | -1.62153 | -55.01599 | 2026-10-04 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af0f46ef-c768-343f-b63b-892aedb0a8e8 | -3.50967 | -59.81022 | 2026-10-04 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 625bf810-a622-3ceb-b34f-44bd2da29b0c | -3.12871 | -53.75692 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ea5014-6bce-32f4-9741-c7782ae8eb72 | -1.24977 | -55.88078 | 2026-10-04 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6eaa1bd-ea05-30b4-ae90-1a1c4d2591c9 | -2.57019 | -54.10884 | 2026-10-04 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cd181a5-7a98-3f14-a07b-e7796b8c82f2 | -1.168 | -49.26367 | 2026-10-04 05:16:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57385b7d-142a-3e68-af90-0ae0f85338bf | -6.02234 | -53.53838 | 2026-10-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65453d67-9f29-316e-a683-af068ccf0ce1 | -4.15465 | -47.53946 | 2026-10-04 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7da3496d-8883-30d1-b254-757b3f9d75fa | -4.15414 | -47.54288 | 2026-10-04 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2274d8d8-1c04-3cbc-9e7a-03a00e0b19a0 | -2.92524 | -53.94211 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fc95ba5-c4b3-3de0-9ada-b378ba63f204 | -3.1104 | -53.73307 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| f2fac998-5d60-36e0-bef3-dca52d17a8e4 | -3.11629 | -53.7424 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83f5095e-3a23-3933-b5a0-47bf2df8070c | -2.96714 | -54.09109 | 2026-10-04 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3f73df2-b218-3aee-bec8-45078a012a06 | -3.29971 | -53.83984 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d04bc63-95af-39fa-924e-269a84372b08 | -3.18577 | -54.08179 | 2026-10-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
