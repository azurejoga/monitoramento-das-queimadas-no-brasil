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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76b25924-817f-3a74-84b5-15ae519907a4 | -4.78873 | -55.70798 | 2026-10-05 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b964a80-a52f-34e4-bf4e-a85a71a1bac9 | -6.00214 | -53.51614 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd3d3487-00f7-3891-b28d-f8d7a61c0bfa | -2.81625 | -54.12035 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df61b997-ce8a-3065-8a19-5e35675270bf | -5.88257 | -52.04141 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 204ed031-0b44-367e-9ee5-f76ff647775d | -3.72383 | -53.42185 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c998e811-59c7-3597-823c-662dc61eb586 | -6.24406 | -52.85022 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b454c60a-b50c-3af0-8ae8-0fbf467bde78 | -3.57045 | -55.41562 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea38230b-a243-3c12-b3e9-43cda13a457b | -3.50036 | -54.6204 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84b06837-ca3a-3351-bc3e-6073b31a526e | -3.39224 | -52.23539 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f88573c-5734-3785-8da1-be714b5dad63 | -7.50225 | -54.98863 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66d4ac55-9c98-3c33-8ce6-97a22f69f487 | -2.36516 | -50.60559 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bf53467-dd66-3f9d-adc6-d8669f1b94c8 | -3.40656 | -51.67341 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe1df698-a8e6-3eac-8827-d91da6aa7406 | -3.91108 | -49.71456 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4412a390-cefe-3ec3-bb40-2f7b8ddef1db | -3.88588 | -55.80355 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8d6f253-63e3-30cd-ab49-9b8fcb723a3e | -3.78794 | -50.86923 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd20a2a6-8650-303b-8b35-0d7273809c2d | -3.27653 | -50.01855 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0fab510c-db51-381a-a6a5-7b024b249d87 | -3.1153 | -53.74194 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d36ccda-b8af-32c2-9bd2-4807b5ce8c51 | -3.11655 | -53.71228 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d9b91a1-817a-36b7-be8e-d82db840b9bb | -3.70812 | -40.34487 | 2026-10-05 04:57:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 545629aa-6724-377f-a8de-085f636aa077 | -2.99205 | -51.04972 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9f7a4096-36ec-32a5-92bc-2928c0a65e88 | -8.52671 | -54.59808 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c677cb5a-8c5e-396d-9688-9ab1dc268aa0 | -2.82435 | -54.11393 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1c3d74e-4fac-3f45-8b53-e901002f9169 | -6.67626 | -55.10497 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6bc8a1e-3fea-382c-b83b-6d39901050c1 | -7.50627 | -54.98549 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fc81c13-918b-3ea0-8fe2-33863205e05f | -3.18457 | -50.53784 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29c8373d-2181-3333-b371-0affa291e2d5 | -6.89332 | -43.68923 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3fb7951-d5a8-3f37-b8bc-99aea6340a44 | -4.30131 | -50.54453 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be648c7-840e-3b25-a25a-4c2b4021ffb0 | -2.90241 | -54.12933 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a6c8829-b680-3816-8b3e-086fc7441e6f | -7.8829 | -44.19282 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efa603dd-f750-3181-99c8-49075288c649 | -2.25363 | -51.93927 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1670005d-855b-3a40-beea-171618732d1a | -3.08408 | -54.18076 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a5292907-8c7b-3395-bbe3-ec2027ec104c | -3.01039 | -53.87207 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5219fcc2-c319-39bc-a42d-907b7a22a89e | -2.78015 | -54.10308 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cda6a212-ddcd-3fa8-814a-e50941ec24b2 | -1.42091 | -57.85686 | 2026-10-05 04:57:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6780703-c772-3c5f-8a9f-0a1bf31fa11a | -2.58117 | -51.8644 | 2026-10-05 04:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b296acb5-301b-3c09-baaa-cb7b6641260f | -7.19117 | -44.31002 | 2026-10-05 04:57:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09f755fc-f731-3e4b-867f-355bb7f0e236 | -3.88011 | -55.8159 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2942dbdd-3268-3490-89f9-e85e2e33227f | -5.99881 | -53.51564 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da802b22-371d-32f7-8557-587729de1cdd | -6.25838 | -52.8454 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8bf7b26-1265-3e27-9020-ff2236abcb6f | -2.80935 | -54.11925 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c5ba6fd-ef0e-35e0-bf6a-0690b88ca16f | -2.9028 | -54.08325 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6d71320-9726-375c-a348-fccec46e5a50 | -2.67889 | -49.02928 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| dca00b80-af8e-31b3-88cb-df6c453bd95c | -2.79617 | -54.1133 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44729f35-804b-3f7d-8dfc-485ecedbdbc3 | -2.9876 | -54.10442 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a157e0a5-2802-3208-8012-4f237beff60f | -3.04358 | -54.21296 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c01c9b64-a485-309e-88e9-82deeb6f7a33 | -2.79576 | -54.09397 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db40e92a-3f10-3552-8ba5-7c12073c850e | -3.10299 | -53.71014 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 79949ca5-c81b-3abd-9122-3d7ff7182c35 | -3.06645 | -49.53848 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df7ffc4b-6453-334f-8210-c9f99cdfd6a6 | -3.09891 | -53.7356 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b680761-32eb-3ca9-b341-dd116f2e6101 | -3.90641 | -49.69823 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3f548fc-115a-31e3-8b30-e9712416531c | -2.93757 | -54.19678 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d2c239e-bd4b-3a30-ad58-d2ea6fdf66e7 | -1.7629 | -55.031 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6e11056-be82-3c6d-9a30-be69307f74d5 | -5.89314 | -57.7555 | 2026-10-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f0da9e4-25b6-3943-92ae-aff0b109298f | -4.81516 | -54.73252 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6069c172-99b3-3e35-9431-26f1a23471ec | -4.5739 | -54.94806 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 30a09985-b372-34d1-85c7-d61afee00745 | -3.27739 | -54.1764 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 691bd675-d132-3a86-95fa-2d3b85b4d7a4 | -3.13019 | -50.34784 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9f27b18-f498-386b-9be7-e86bc2386e72 | -1.63091 | -55.13162 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e7ed2f7-5655-3828-8604-b62e5e8d9bf7 | -6.90691 | -43.67027 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de9032f5-a04e-3a58-9b14-4de093c8c56f | -2.69253 | -49.0355 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5a6a4e27-c061-3cdb-9040-5ecf6bd1bf53 | -3.00357 | -53.87097 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c6ff7c1-c687-3533-8a9d-280828015f23 | -2.88424 | -54.09264 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d4aaa6-fbc8-3a11-9eda-1e14c7af24af | -2.99138 | -54.03605 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a2cf37d-5880-3eb5-95c2-44fd889fb5b2 | -3.10967 | -53.73358 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e68f403a-e90f-3b17-a905-3c7d05fafea9 | -3.12392 | -53.70972 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7be80b8f-ea21-32bc-8b0e-7265e269136e | -3.59513 | -54.3178 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b3d2a76-c1b0-32fe-9eaf-c05199d0263a | -2.7785 | -51.36917 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb020568-a113-37c7-958d-36c3db18a327 | -3.30613 | -53.84291 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2f312d7-d727-37b3-b6f8-db589d1b7b70 | -2.98997 | -54.75231 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 640faf88-e788-3f36-93bd-77cc00508696 | -2.98452 | -54.03497 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8eeed87c-1739-39bf-8c76-1a8147949497 | -2.80833 | -54.10367 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcea799c-ea02-316a-a4f8-7c1e8b84755c | -2.80875 | -54.12301 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf1cdc7-3df8-3e00-ba68-d5d4ed80c5ed | -3.05784 | -54.2346 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5909feb1-4f57-35f8-a0c5-acd8c9f46850 | -2.9113 | -54.09614 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e46fbbd-d2c4-3f65-96b1-8d156daa630b | -3.30214 | -53.84602 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb250512-6870-387d-befc-b7eb3173a502 | -2.78644 | -54.10792 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b81ce586-015b-30be-94b6-af89ada02bf8 | -3.15809 | -50.44118 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ed02c1c0-19b2-3fb0-8bd4-999d75621bbb | -6.08017 | -53.30373 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce9f662-6877-36a9-9ba9-db3a050daafa | -2.96531 | -54.08934 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7425f7c-b0a1-3470-aab8-57642a99ad96 | -2.48881 | -56.10023 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edc2cd1d-2d09-38ad-91f6-7e292cd98404 | -4.26244 | -50.79157 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3b0de6f-aca0-3e37-82b5-1678814ab928 | -2.89674 | -54.12072 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5525a666-439f-33f5-a6d3-e98907641a9b | -1.98607 | -50.51447 | 2026-10-05 04:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a83a505-9fce-30a8-825f-f9fef0d37229 | -2.59746 | -51.84977 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b078156e-827a-3ce3-93c2-839fb03f98f7 | -3.09785 | -53.72051 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 34394cc9-db6d-337e-9b8b-4a2efe6e9f08 | -2.94855 | -54.1059 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 469ee8a2-4120-3720-b003-61852e3c9034 | -3.02332 | -51.45394 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 982f17a3-0267-3151-80d5-39d1d73680dc | -6.21241 | -52.83512 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79b0226e-11bb-342f-9972-6718e4a39e3f | -3.12441 | -53.72845 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe004e7-6212-3063-8074-aee869db90b3 | -3.28291 | -53.83549 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dd65d73-0856-35e7-bfaf-7089f02a7024 | -3.00698 | -53.87152 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d93b80c-fd98-3bfa-80c1-cc51effec358 | -3.10124 | -53.72104 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c5353dd5-0bab-3a6c-a0f5-77cf7ef0f205 | -2.94508 | -54.1941 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c61bdc0c-3c5f-30d1-951a-1e2eb8b4e270 | -2.99604 | -54.17849 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71f97609-e838-3bbe-92ef-68b071abaca8 | -7.50567 | -54.9892 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfa97f97-8f1c-3832-8edb-c4a44f4bbf1d | -6.90056 | -43.67649 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7a33369d-7386-3452-b366-f9973d9824d4 | -2.85255 | -53.916 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57f3ba61-e760-3b58-ad81-c3a918302e43 | -3.86605 | -55.80911 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a683e811-77f0-3c99-b3d4-5403f27f464e | -3.91926 | -49.70799 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8620bd9f-685d-3f56-8990-cfc407c0328a | -2.92756 | -54.14878 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README35.md)
