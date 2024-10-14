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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a282f3f9-30b7-368e-96af-7568d4562d2d | -1.71994 | -55.22205 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f469eee2-8f2a-3c3a-a584-b957f2e6f0e2 | -1.71829 | -55.14952 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2766989-af94-36f6-997f-3c86e3da9304 | -1.7155 | -55.14549 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62a688b9-67e6-3b4d-8cd9-908aa08267ad | -1.66713 | -55.19206 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd3bfb50-408c-32a5-8010-bb11de435b2f | -1.65421 | -55.40503 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db98a09c-c787-3f5f-9b20-634f0cac0137 | -1.65267 | -55.19704 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1b0f753-9104-3b64-baf5-977d1b41640c | -1.65189 | -55.09234 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72a35dcb-30c6-38be-9a4e-14b829e9ceaf | -1.65134 | -55.09587 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19a05859-fdfe-3f44-8685-a32ebbc8d0b6 | -1.64854 | -55.09182 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0c8d0c0-4650-3b91-8f4f-1d2bc587b3e0 | -1.64799 | -55.09536 | 2024-10-14 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7713c2b1-6d29-3e05-bfee-f4c6d0fb655c | -1.34788 | -56.03564 | 2024-10-14 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d063729e-f6e8-355a-9a57-165854d56d93 | -1.34458 | -56.03513 | 2024-10-14 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be563642-9bc9-3c94-b5e0-4929f4d5dd80 | -1.34404 | -56.03856 | 2024-10-14 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c10cbb-f3b7-3e06-af10-848e3e0c74d6 | -1.33609 | -56.13216 | 2024-10-14 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b645d8a9-4808-311a-a7c1-a3841f045e88 | -1.26294 | -55.90635 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42533efe-43a4-352f-b0b4-b6aa3c0ec7e5 | -1.23267 | -55.90518 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d86d4fc-b0ed-3b28-ba62-f2e75565e5f2 | -1.22937 | -55.90466 | 2024-10-14 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 709ca05c-e299-3736-986b-24fb9efc3ad9 | -3.47471 | -55.4046 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de9108f9-eef1-399a-bee0-bd3ae8741d49 | -3.92767 | -56.02807 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aede5607-3c54-372e-ac22-97405b9902ea | -3.92713 | -56.03154 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23ae20e0-9ba6-338e-9816-b6476d8c24cf | -3.92659 | -56.03501 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 001c39b4-d7d3-33df-9714-bc3feb4787ab | -3.92546 | -56.21593 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6af5d3af-2c13-3741-9c13-eb94ad45e071 | -3.92381 | -56.03102 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a035e07-ecb8-3526-b1bf-fadb4743ec47 | -3.92327 | -56.0345 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7784a3fc-a3e0-3bfd-901a-1029c7e46a16 | -3.9216 | -56.21888 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7fd21a-5740-3df3-bf9e-9a1ff314000a | -3.92015 | -56.09802 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c85116-981a-3151-81cb-27a7e6e034f4 | -3.9196 | -56.10149 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c22dd11c-ab02-368f-b442-7717f46e6f27 | -3.91871 | -56.17234 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3bde964-8e0a-3dec-b29e-5e5e8053d1f3 | -3.91683 | -56.0975 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79d00771-8bb5-3cd7-a3f8-cd8da9a9e81c | -3.9154 | -56.17183 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 532c9051-c5f7-3b16-9002-c88cc7fa3d6a | -3.91358 | -56.11831 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d9c63de-35f0-36a6-a8c9-9b7e5a58a38e | -3.91304 | -56.12178 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb19ed61-2644-377e-b783-75c6a38d87e3 | -3.89588 | -55.8201 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf28be9d-3cc2-318d-94b2-355326562cb8 | -3.89255 | -55.81956 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa096264-5aef-30e7-bb13-f20a8d1729e8 | -3.87927 | -55.83903 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eac06405-fec0-384f-9743-5af86da44022 | -3.87581 | -55.77388 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 146aac62-8654-393c-bc65-315987badb0d | -3.87303 | -55.76985 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0726e19a-530c-3bb0-8ad5-c1d096594551 | -3.87248 | -55.77337 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1f9a5d1f-bd1d-3f6b-a51d-163e7ad6cf0b | -3.86914 | -55.77285 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68e2ee77-6fba-3f60-b639-5c5e9832d2fb | -3.8686 | -55.77636 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43eae1ef-1abb-34f4-b0fa-01ffe426741f | -3.86297 | -55.74676 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9a3ce72-f35b-3b56-9a8c-945395d27945 | -3.85963 | -55.74625 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96fc3d85-d1b1-3b9b-9730-282412969a99 | -3.85089 | -55.80236 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53be56d2-4f6d-3760-a5d7-02957c04ad4e | -3.85034 | -55.80587 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 038e2d21-3fc8-3531-a09a-6822abbf5992 | -3.83308 | -55.98194 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fc68488-e7c8-39ba-9050-b3cc6da42311 | -3.83254 | -55.98542 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77d6d1b0-34f6-3b9c-8d96-fcfcd3cc1080 | -3.83199 | -55.9889 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0b718c84-10f0-3a5f-9c02-cf290d3d7fb8 | -3.82976 | -55.98142 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 315ba256-8f65-39f0-95fc-7fc1f72aa529 | -3.82922 | -55.9849 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4049a26-e901-3563-8ea5-f1d9cd86466d | -3.82867 | -55.98838 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d4a6ed6c-2c44-3cd6-861c-b3aebceb5346 | -3.82813 | -55.99186 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9e1af74b-0602-3b50-b3b0-b3e919c9b245 | -3.82535 | -55.98786 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73d9b76c-8265-3991-81d9-4e1c76a9b607 | -3.80786 | -55.88167 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c88f9519-8eb8-3069-892b-431feb69f361 | -3.80453 | -55.88115 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d98de86-d401-35fe-93e7-f1ca267d9873 | -3.68708 | -55.95895 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1786a38-6fb9-3566-9513-83285207eb3a | -3.68376 | -55.95844 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06bef8e9-df56-39d4-b9fc-25e7a198de24 | -3.68322 | -55.96191 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b64f409-9562-3d30-9874-91ca83f340cc | -5.00606 | -56.21323 | 2024-10-14 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 986e11f5-125d-37a5-9625-cbd29641aca0 | -5.00551 | -56.2167 | 2024-10-14 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c2ee77d-ea7d-3fac-bacd-442ef3b1707a | -4.8081 | -56.15426 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e7cedcb-c0ea-3425-b184-f1f730e9bc0a | -4.80755 | -56.15776 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4784865-5ccc-39a7-8678-46f96c0a05fb | -4.53413 | -56.18992 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0ba191a-080a-323c-a4cb-86a90c30df72 | -4.32217 | -55.61111 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| ebc19fbd-b0c5-3e0b-a883-8257dd6d36a1 | -4.32161 | -55.61469 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 8841ff4f-9229-3c2b-b2bc-617876fef9aa | -4.26291 | -55.77215 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de080dc8-1820-3bef-8900-78c169d8c332 | -4.26011 | -55.76811 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf3feaa3-d91a-314a-8613-5292e3c79705 | -4.25957 | -55.77163 | 2024-10-14 05:08:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaa7eda7-fd03-367d-a8f4-fdc781be7877 | -4.14656 | -56.27894 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c45d94c9-9eb9-3da6-b2a0-f64931679531 | -4.00179 | -56.05408 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bacee3c-0ee1-3964-b56b-ca4c08741cfb | -3.99072 | -55.73346 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c84a733-cfdd-394b-8ed7-a80c535cb18e | -3.99016 | -55.737 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98839045-bbb5-30a3-a11b-575e05124d3d | -3.98961 | -55.74052 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae441062-c9d8-36f2-aaea-e93edf137952 | -3.98738 | -55.73295 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a626caee-248d-3f95-9c24-c01f037bd475 | -3.98682 | -55.73649 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de785705-7a67-322b-b540-cb0aed108b57 | -3.98628 | -55.74001 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7432920-3a1a-39c5-9198-73cb0a777a77 | -3.98349 | -55.73596 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9756551d-fa4c-38f0-903c-1c4e3e25e2c3 | -3.98294 | -55.73948 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ebbe45e-ebcb-3458-b0a4-a2796472adcd | -3.9796 | -55.73895 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3a05901-7e07-36d9-9930-29974248bc2a | -3.9655 | -55.65369 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e742499b-8d81-38c1-b0a0-a159771300a5 | -3.96495 | -55.65722 | 2024-10-14 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 629538b1-7f41-3493-b47b-7c64653f16c8 | -6.27738 | -56.53244 | 2024-10-14 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8560278d-704c-37cb-83ca-7483641a0358 | -5.23667 | -56.0625 | 2024-10-14 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dacd6f2d-c323-39e5-9863-f63058f99880 | -5.20717 | -56.05449 | 2024-10-14 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f7798c-3d0e-39a3-bdf7-695db911882d | -3.67861 | -57.01001 | 2024-10-14 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6753a7c3-5578-3bd0-b7e6-6fe7ad27626f | -3.43281 | -56.95351 | 2024-10-14 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 719a8ef9-a75a-3add-b0df-bc0e31d31cac | -3.41644 | -57.0144 | 2024-10-14 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eaecbbe-aaba-3f42-99c6-5eb914ca2a3e | -3.03856 | -57.38381 | 2024-10-14 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9500286f-e5f7-3087-8561-f55dd608a5e7 | -2.9411 | -57.1413 | 2024-10-14 05:08:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c5f4251-a083-3735-be41-f12cee424de4 | -2.73403 | -58.04159 | 2024-10-14 05:08:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85e4cad5-67ed-3a9c-903d-72b30456ac29 | -2.54207 | -58.03378 | 2024-10-14 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e628efc-4852-320b-b2cc-c491f927aa34 | -2.53869 | -58.03325 | 2024-10-14 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30a61936-847b-3717-aad8-ebfb052d897a | -2.53531 | -58.03272 | 2024-10-14 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 994a3283-3004-3638-b81f-7fb37bba45cf | -2.32532 | -57.98575 | 2024-10-14 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ed87c586-3c0b-332c-949e-9ec4fc75482c | -6.45819 | -58.46904 | 2024-10-14 05:08:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ea41b62-7b19-31b2-9a9f-af2b6ff54c69 | -6.35134 | -58.18122 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083b493b-e4a9-3042-b05f-4a90a0eb3b7d | -6.34857 | -58.1772 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 007955f7-f12b-39be-b148-a2cb9027df41 | -6.34746 | -58.1842 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba32e781-0c92-3808-a01d-94195f57c652 | -6.34691 | -58.1877 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2fd4b5a-d97a-38af-bced-266a1e911c1d | -6.34635 | -58.16967 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37171159-6378-36f4-9a8b-3f0388a8b52a | -6.3458 | -58.17316 | 2024-10-14 05:08:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README104.md)
