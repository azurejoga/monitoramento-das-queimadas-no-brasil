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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 107e5bcb-b59a-3b71-98bc-94974f8bf370 | -6.60309 | -56.36971 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c161f729-af6a-328b-98ed-cfe84eb0cc78 | -6.24828 | -55.62038 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e6dd21e-826f-3f4c-9f25-410d04005fbf | -6.59125 | -56.35689 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da760a71-4f1c-317d-9fb4-54506bf9ade6 | -8.02473 | -55.11944 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7f88806-5d03-3667-9595-e20dc9198342 | -7.26778 | -44.70079 | 2026-08-15 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1ee3c83-21f5-3adb-9dbe-3af26a2c1ced | -3.74518 | -59.33194 | 2026-08-15 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e6483d5-1e84-3d38-bace-5ad632854cc6 | -6.79533 | -55.843 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3095b982-fd25-3df8-a0b0-964aaba2246f | -1.58955 | -50.44323 | 2026-08-15 04:57:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da9e5568-58ab-3c5a-8a72-22ecf16f2f31 | -9.13434 | -46.3981 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d537c414-432c-3ffe-a769-4690dfbc900c | -6.11211 | -53.07507 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11259085-7a7c-34a6-9e13-f818cf79de0e | -7.06023 | -56.51933 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e3fe393-075a-35f9-9948-59bb585fcec7 | -6.57394 | -55.15259 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e0497ed-8c14-369c-b0c3-3eb79b610b21 | -6.8489 | -56.43573 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20476861-8454-3eec-832f-bdac4d4e0289 | -6.83011 | -56.42126 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6dc8a70-ddfc-39fb-8a8a-4d1f9841f022 | -8.16828 | -47.40415 | 2026-08-15 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b64170fa-f7eb-3fee-9bf8-bd7202bbee3d | -6.96843 | -59.29272 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff13c4e0-8158-3c4b-a5d7-4dc14862e14a | -6.78464 | -55.84503 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6535a1b-db31-311f-a6ea-40f512b25705 | -9.11825 | -46.40195 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9c896ed-e14a-330a-ae55-70b291d0ad7e | -9.14027 | -46.39262 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62ba9ab2-73d0-3a95-bd79-86d3e5c3761d | -6.61888 | -59.06652 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 09183d1e-cecb-32ef-8dc4-aa9c455e4fbe | -6.79419 | -55.85023 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c3504bc-d64d-3640-819a-665faf070f32 | -6.53625 | -55.17543 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33ca9ae0-c67a-392e-8ac2-d5caa88cbef4 | -6.83071 | -56.41753 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fc792c3-4ac9-3a5e-91f7-b647b0c6eae3 | -6.61358 | -59.04987 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 504f628a-4b7b-3078-9145-27608f2cf33c | -6.58967 | -59.00157 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 033aff0f-a9b7-3a56-a945-e0d66d5c1ad9 | -6.74221 | -56.40004 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a96030ec-0bef-3caa-9b25-3c6059469bbf | -2.5154 | -49.36004 | 2026-08-15 04:57:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10f48e4e-416c-31bf-87a3-fc075f06de06 | -8.75652 | -49.4154 | 2026-08-15 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9de04fc6-a649-3e82-933a-17107026f93d | -6.60381 | -56.36643 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbf15b2-e66c-32e2-9b6a-73d0e9bc55fe | -6.85937 | -56.41441 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37fb4ec5-85b6-3827-9d35-ac59d924ffb7 | -6.60214 | -56.35475 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85e89456-5811-3a87-a0b7-8fda0b6cdaae | -6.85354 | -58.96502 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db7fda69-a982-374e-aed5-9a16bfa2d537 | -7.69697 | -55.17066 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d10b2b7f-668e-36df-96ae-d6c064c6f41f | -6.93544 | -44.54414 | 2026-08-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cff2dbc-48e4-3c92-a364-53ffca55e779 | -3.26155 | -49.52338 | 2026-08-15 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a0c70a6b-dbf1-34de-bfc8-ce50457561e1 | -8.4883 | -44.73889 | 2026-08-15 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| afe23445-e46b-3743-9eaf-e2e2d70c6d85 | -6.62316 | -59.04105 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3b322c9-07aa-32fd-8485-756424987215 | -5.95309 | -52.26281 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a807a648-e09b-33dc-861e-7e4cd75cf921 | -6.12277 | -44.03034 | 2026-08-15 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 064544e3-2556-3845-b20c-e0900e80d8b3 | -4.10597 | -50.992 | 2026-08-15 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a6338200-e9c3-38dc-b618-da2fec1e2e72 | -4.25029 | -48.54491 | 2026-08-15 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86fa116a-31c3-38ab-8d41-8ecdf2531ea8 | -6.79626 | -55.84732 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa18bbf3-7d49-386d-a3cc-38600f5fdb59 | -6.84727 | -56.42397 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9ca1201-c3b8-3d6c-9ea9-f5c158ae6be8 | -6.82586 | -56.44749 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9da31f4-64e6-34a5-9d16-52eacb0395ac | -8.10532 | -51.65773 | 2026-08-15 04:57:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 481d22b5-93c7-348f-857a-021e9a87024b | -8.02586 | -55.13386 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d86ef568-5e2e-3459-8849-5c506d7bbba7 | -6.34516 | -49.89902 | 2026-08-15 04:57:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55cb4355-ec09-3c59-acd6-749565e99d89 | -3.43197 | -49.47525 | 2026-08-15 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4b1d58b-01ed-3fd5-87e6-8e1f436519e2 | -6.61572 | -58.99023 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e5cf868-9b23-376e-a95c-9cb50034bca6 | -6.61444 | -59.04479 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56cc7ba5-e459-362d-b548-ce501ff4cd6d | -6.83637 | -56.42609 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 149f9b3e-2456-3e34-9590-1cc8e98f9b07 | -9.11277 | -46.40419 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1bd1cd8d-1663-3c8c-ac96-fed352859852 | -6.62231 | -59.04612 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fbe8d133-705c-398d-8a3c-81fa362ff0c3 | -6.92911 | -43.6368 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a76a74ff-bf27-3b4d-b55e-a1736dabec6a | -6.58378 | -56.35962 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23285020-42dd-352e-8d8b-522ac09b3e5d | -7.2758 | -44.68311 | 2026-08-15 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6229e29e-1f13-377b-8a33-240522f05081 | -6.84667 | -56.42771 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 42595398-fcf5-3534-85ff-4853826d2431 | -4.10889 | -50.99661 | 2026-08-15 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28382d80-28b5-38e8-93e1-436e3606b457 | -6.96445 | -59.29206 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8feff40f-5715-311f-ad47-190933693716 | -6.93505 | -43.63758 | 2026-08-15 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 81081656-2dc3-3468-beb2-591e99a228de | -6.60431 | -56.36219 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5a070a-7042-3c21-a8b9-437216b5dcdf | -6.94053 | -62.88316 | 2026-08-15 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9122ebd5-9171-3623-97e0-f08fe2bb8d76 | -7.42086 | -60.5171 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 573e0b24-474b-3968-8bbd-a8e8c4d15456 | -3.72256 | -55.96671 | 2026-08-15 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68147211-3840-3543-a45e-98cae14145ee | -6.80105 | -55.78477 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 135dba3a-2057-3116-a87d-8f5ed230acb2 | -6.24761 | -47.712 | 2026-08-15 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85ec783c-3266-38c2-ae90-268084481396 | -6.22914 | -55.6541 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c888d826-b404-3965-b2ec-fee5d32e53fd | -6.60636 | -58.99689 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a04cb5ef-96a4-3595-ab47-13262661928e | -2.40866 | -51.8369 | 2026-08-15 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa95c389-9f3a-3a8c-822c-904ed08f7848 | -6.62118 | -53.41037 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc90a417-e258-3ad1-b0a0-a9bc4fd284d8 | -1.82362 | -47.89793 | 2026-08-15 04:57:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41d7129b-7ddb-38c0-baf1-60f7ed33ca23 | -9.12376 | -46.3996 | 2026-08-15 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1b5d298-e555-3e75-85d3-12b763b96ab7 | -6.96615 | -59.28175 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc44f4bf-ae9d-3ab4-b907-b9bb7dbd5810 | -4.10973 | -42.50449 | 2026-08-15 04:57:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2e4c80be-dd84-3c9b-a096-dc1db0813d31 | -6.84324 | -56.42717 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e68f9368-bd12-3efa-ac46-7946ff140e7a | -7.73 | -46.24463 | 2026-08-15 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ac9b12f-7fb9-3ba9-8da9-c42454c094fe | -6.86117 | -56.4032 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc0948a-25f3-3cf9-9850-58bd2bfa09bc | -6.60677 | -56.34774 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51c39881-99ea-3e18-93ef-be20af931ff8 | -8.0264 | -55.13039 | 2026-08-15 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d0a142-b73c-314f-9eca-867279ceb609 | -6.95193 | -59.29358 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a7f3d19-80c0-3acc-a0b8-36334e47a519 | -7.39084 | -59.99625 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4badbb0d-8fc8-37a2-a13e-21841955395d | -6.78858 | -55.84195 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 772f2c0a-e58a-335e-b004-3048b30c0cae | -6.94101 | -44.54514 | 2026-08-15 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8038432f-17f8-34ad-8fba-a5534df93f7b | -6.61115 | -58.99245 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bbb3807b-09e8-3261-9642-8b763a9d5e04 | -4.31315 | -59.46572 | 2026-08-15 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1559365a-8c6b-3c9b-a453-9da922dbb952 | -8.71764 | -49.60529 | 2026-08-15 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cd3b56e-dc0e-3f67-bde4-f0a1ffc641a7 | -8.16896 | -47.39907 | 2026-08-15 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c73c5d81-b342-32c1-a7aa-cdfca91fb5f4 | -6.81959 | -56.44268 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bdaf453-4b56-373f-8bd6-4df083b8d14b | -6.63765 | -56.2646 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 860ecc71-656a-39bb-9140-dee73d67e1d5 | -6.81615 | -56.44213 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eee2c2d5-269a-3181-a3c5-1e2822c5b7ae | -6.59066 | -56.3606 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94077fe2-0908-3fdf-b34d-87a9a962eb87 | -6.79767 | -58.76706 | 2026-08-15 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d582a16-1146-32dc-84bd-550bfe6125f9 | -6.79703 | -55.83218 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d837369a-4c57-3e98-aa25-1db740455d63 | -6.2693 | -43.27668 | 2026-08-15 04:57:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 38e61c7c-bcdf-3bfd-a9e0-37b7e765d9ad | -6.58094 | -56.35537 | 2026-08-15 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f0bf5f4-685d-37fa-b187-5798cf0cb83c | -6.69707 | -58.96024 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 267f17d1-003c-3f7d-a8f8-fbfcc68c9c45 | -6.79503 | -55.69189 | 2026-08-15 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 520da82a-af51-30e4-808a-a9698b1cf52b | -6.60147 | -59.00344 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b9c06874-64b2-31fd-aa3d-859c470d4f74 | -6.85438 | -58.96005 | 2026-08-15 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e88fa3a-2f2f-3aa5-bc04-a7dfce83a5b0 | -6.02756 | -57.82226 | 2026-08-15 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README24.md)
