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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b255bec3-b7ff-37e8-89fb-61bc2d042de2 | -13.16757 | -54.31706 | 2026-10-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8b143cf-c4fb-37fd-8e97-32afe20fa5d9 | -4.93448 | -55.80974 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a829c87c-1f0f-3faa-b0f0-4f76c2ec13b1 | -3.52852 | -54.6505 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3acbc95f-abbf-38df-8532-0c008425876c | -4.4442 | -54.97509 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dd6c021-500b-36de-9310-d1e647cf288a | -11.31451 | -46.68553 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d105b493-e47d-3f00-bfc0-28ad289ab065 | -3.66782 | -60.62272 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef6aa9ff-520a-307c-ae38-689334559a2a | -3.08446 | -54.2476 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabcd90b-5e82-39db-b16e-9b34cba05433 | -3.28948 | -54.06494 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 642b440d-3a35-3c7a-ac57-2545d17bc234 | -8.62382 | -67.02425 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fee3ecd6-d94c-38ca-8f0e-df9aa3d6a3fc | -3.54276 | -50.09863 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f619ae5d-8061-35a1-84c5-4d449fe4bf7f | -3.22744 | -54.30017 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f2e02d52-b415-302f-9154-499f3f1d41db | -3.85322 | -55.97742 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c64358c-c5b9-3555-85ee-4d7fa7b9c913 | -3.26377 | -54.04489 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8830aa06-f641-32d3-80c2-784cbf4dc324 | -3.70429 | -50.65661 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cb2094d-d8d0-3b73-a143-9deb7b31baef | -3.09513 | -53.71682 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8de8f0f7-a189-3514-95ec-796dd69b1dcc | -1.60473 | -55.15995 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b8a597f-8d2d-33ff-b782-6e90ec892011 | -4.15288 | -54.91511 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb7e845f-5058-3215-b408-3714999eaabc | -2.78698 | -54.00631 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7076b91-2310-348e-be31-ebe882dffb6c | -6.14511 | -51.69964 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e708f259-5bef-3463-8910-01337522426f | -4.1152 | -59.88187 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 12c90e28-69ed-3124-ae2d-6e17cfa41c7c | -8.52298 | -67.0015 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 666696cd-f07b-36c1-8f7c-fbf44b7d7dc6 | -3.63077 | -55.51342 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d29a380e-9b45-397d-a1df-6e818a885af7 | -7.22127 | -55.12408 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b19aafb-34a1-3e2a-9359-fea2c2a40680 | -4.4482 | -54.97198 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9908aca7-ea98-3a30-a1fb-709c9cfbb0f7 | -3.59477 | -54.67165 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ae19c02-7be2-3283-ad12-2952a12d9ba9 | -2.87263 | -54.19622 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 89e93e53-1100-3bd5-815d-87266f55fb5e | -5.67997 | -53.49051 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c439b7e7-2cba-3e9f-9a39-56d502097103 | -2.48516 | -56.09025 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f4ead9a-5429-3a04-97c3-0bb904361122 | -2.99398 | -54.08878 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1fac5eef-728f-3bd7-beab-b9ee7e811a61 | -3.15641 | -59.08817 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b64a1e1c-6897-3c21-9524-196499298c91 | -3.28657 | -54.06051 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d729aeda-38ed-31c7-9f18-f78d276112b2 | -3.0515 | -54.15705 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3315ab3-70ac-3678-851e-422989940f15 | -2.78501 | -51.67125 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 920f5b7f-0cc7-38f6-bca4-58dfd0cced83 | -3.47425 | -59.57828 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0bc25096-7e9c-3a42-a2ad-0ab01d8509e9 | -3.29088 | -54.03313 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d3b3bf3-3331-38b3-a007-02e307166c9b | -3.22337 | -54.3034 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b117d43-66a3-3fe5-82f2-08e81f64dd52 | -2.5165 | -56.25806 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63d4a307-e697-36fb-a4e0-687cb9f38b3c | -2.78422 | -51.67638 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a250b88-f041-32ca-b8c0-7b7b3d0b7fb8 | -2.86018 | -59.11161 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb867c75-cfc5-3869-b2b6-2d7827ff140c | -2.89663 | -54.15678 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23505016-3c2e-382a-b440-fab5ef1c1474 | -1.33468 | -52.43947 | 2026-10-08 05:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c54fab3e-252a-3fd6-8b00-42ede9b4d239 | -4.69635 | -50.64131 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca12062d-3d80-395d-8469-9832cdf8d0b3 | -10.61443 | -60.4857 | 2026-10-08 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2025d5bc-9f41-3c4c-8d75-e0033e0d507e | -7.38533 | -55.2069 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 269ae1ce-a932-312e-bde9-c5b6776fbcb6 | -4.00874 | -56.25489 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ccb6b5-0e05-3ef1-9dd5-e18f4cea5788 | -2.30427 | -58.09971 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73f08527-02a2-37cd-a1ba-6a9626b4ac99 | -3.58555 | -54.68553 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ee92d696-e9cb-3581-8e6c-37b93a843fa3 | -2.98415 | -51.24416 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8784c097-ac6d-3641-877d-8c60fed03b61 | -2.58125 | -56.14411 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ed19fc4-1232-30c6-b2ef-950284f00d16 | -4.61011 | -55.71911 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ece5d9c6-f4c0-3b7e-ba8f-9462c78f32e3 | -10.71749 | -56.04629 | 2026-10-08 05:23:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf5e1bcf-94f5-3c32-80b1-abe772ee0381 | -3.54232 | -54.65258 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98ebcf01-4974-3bf3-9720-60b283d56b91 | -4.79874 | -55.69762 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65cb2a1a-b5f5-3bd8-8a6e-4773e7b52948 | -3.97127 | -56.12427 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da772de2-8ac9-343d-ab44-24cad8de8624 | -3.07744 | -54.26994 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbe91cf1-dd77-3161-81c5-01291b390e86 | -8.61517 | -67.02646 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 34b3e20c-42ac-3863-ae69-b8da81c9a225 | -12.10282 | -57.15648 | 2026-10-08 05:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b441fb7-6612-34d7-a822-001b8922a52b | -5.85618 | -53.46568 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 240344c7-d20e-35ce-bb69-1b37e9e9ea8d | -2.998 | -54.10923 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25b1010e-5867-3332-84c6-b69fd29816d5 | -2.93385 | -54.17042 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231e38cf-0a60-3451-b453-bf2ce5699029 | -4.11498 | -59.88431 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbe83a38-10aa-3704-b49a-fb0f1f9a2ebf | -2.76387 | -54.10958 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 056eb8f8-2474-3d72-b373-3c526b980990 | -4.17231 | -56.35204 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d6b2bd3-aa15-39b0-962c-da3ab961af7d | -3.26466 | -53.99291 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e69ae5b7-f47d-394a-8f79-1a1734310638 | -7.38475 | -55.21077 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b213e98-6202-3f61-b104-7e12860131ec | -3.12391 | -59.04284 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86931ba9-04d5-39ba-bb92-e21da619d93e | -3.52213 | -54.66864 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce61b6f2-36bb-3c06-94e7-d556387600a3 | -3.32505 | -57.96144 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9543666-40b5-3a4d-a6d2-44fa93089084 | -3.64935 | -54.27618 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a0a485-f430-36fa-a010-73b2acd92816 | -3.63095 | -55.45901 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01aa8f77-3005-3c68-983f-6e8cc325031f | -2.78501 | -54.06553 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f2f1cd6-5f79-353f-9aa5-e646dfd84cd7 | -5.34394 | -50.98548 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d43facd-6672-3bcb-aabc-c9c3a2140ca2 | -3.00065 | -54.18451 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0616449-e6a5-366f-937b-feeb3999c982 | -8.71371 | -45.18145 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2978e7eb-5150-33a1-9355-d6a57618b33c | -7.20736 | -55.09814 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 412cd45d-0042-3a71-90bd-effc26d8eca2 | -3.53253 | -59.49931 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efddec24-b7c5-3016-9105-822d22e3d991 | -6.2185 | -55.67536 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed613431-df1b-39b5-a04e-80711f1025b2 | -1.28712 | -54.56593 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5c5c399-d62a-3612-9803-c6e5d7bff1a5 | -3.05168 | -54.22397 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 214eee24-3a46-35c8-b355-f7944fe07424 | -3.27034 | -54.02597 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9408e0f7-9d15-3cc4-9d3a-c1bfefdd65dd | -3.51225 | -59.31977 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3edb65f8-1bda-38dd-b29d-e9d478ea64f4 | -3.62854 | -59.56471 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed517bc-1209-37ee-af1c-c98af94c63be | -3.28982 | -54.01691 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68ef74d1-a5d6-363f-95a7-8dd02a8ba64e | -2.82849 | -54.13145 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 664065e5-2f16-3096-afbd-3eba40e2cc0a | -1.20796 | -55.69812 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36ff60b9-d555-327d-ab0e-83faa456d120 | -4.34369 | -56.25404 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54c575eb-9f3b-336e-907f-56e3854af305 | -3.01753 | -54.05273 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 390141ec-d0d8-383f-86de-6ea8122d38ab | -1.47581 | -54.54304 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1016382-9ea9-3d96-928e-8e3bbec3a02f | -3.10926 | -54.15685 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90084cf8-cca9-3ff1-bf55-3d62e7534a76 | -2.95277 | -59.16157 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c9bb6a3-b7e3-3ca0-92b0-d9c6fd0ea511 | -9.49342 | -64.35539 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf16d3cb-5172-36f5-9995-f9e68e08b9f1 | -3.59836 | -61.63261 | 2026-10-08 05:23:00 | NPP-375D | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9354183-4894-35aa-b111-2b8970b7e776 | -6.21066 | -52.79076 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 894cccb8-6ac0-3f85-8117-2ce1f96280a7 | -10.07982 | -55.16047 | 2026-10-08 05:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a1e8f85-4c37-3227-9923-54b3025a4cfc | -3.26926 | -54.00975 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2cea9e5-ba95-3dff-b36a-f1087fd8d7ff | -3.01736 | -54.74732 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8acc826-f3b8-3185-b609-607ccd6494f9 | -2.99577 | -54.07717 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 05d3b877-d4a6-3fc9-ac41-c01abac35a9c | -3.06802 | -59.27693 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59baee90-59a3-3664-948f-1c210a4622b1 | -2.40143 | -51.31155 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a1b71f-ee20-361f-9449-e5935b602d4f | -3.01562 | -54.08821 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |


[Clique aqui para ver as próximas entradas](README137.md)
