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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89aa2fd2-e629-3914-88dd-1a8cafa87a07 | -2.50005 | -56.12201 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bec06674-cd8f-32d0-b220-53567a89475e | -6.10086 | -55.72375 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6475c7f0-98d9-3982-86e2-1604d87c2346 | -3.01263 | -54.09959 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 23d5c885-1d64-3cdf-aeb1-f6dfa8161994 | -3.30255 | -54.03421 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62aee8aa-5a30-3e0b-82f6-26d284a70b03 | -3.52447 | -59.35579 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8568c31-147a-3014-8570-1466ce51f73d | -3.58013 | -54.67994 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 262e4225-f880-39e9-b876-58a9584061ec | -4.15109 | -55.13776 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4588121-2e73-39d8-a18e-d662f6cc3813 | -7.21486 | -55.08662 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfc9d65e-19b7-3cc1-a591-5ec80721a039 | -3.96301 | -60.00039 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e96ef64e-486f-3908-a190-3e885268ae23 | -3.17654 | -50.5518 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0125281-1fe2-349b-9018-8bfd5703790a | -2.75868 | -54.10998 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f29b7fdd-3fa1-3315-8a25-f914029800af | -3.09083 | -53.94436 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9c67d35-3590-31d7-9e51-740b5f16affa | -3.28187 | -54.06207 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ae1eef-551f-3fe6-8df1-66a2d4bfec6f | -3.99985 | -56.24754 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7f8bf37-a438-36f5-a3cb-531879a00fdb | -2.89761 | -54.07797 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 243f87ae-6101-37bb-b6fe-8471f1831978 | -3.02472 | -54.0914 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47fcd124-8d2f-356d-98bc-4385c330bcc8 | -6.72932 | -55.11109 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285a36ac-dc9a-3536-86ab-25a8462747c8 | -3.74232 | -59.47285 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a385a0e-80f8-3f1a-b806-59dbfb44f694 | -3.02756 | -54.10849 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2e24c39-4731-381b-9aef-cd83ee4d2b09 | -3.0798 | -53.9637 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 7bd2fbce-e361-3434-9c8e-b5edac129aa1 | -3.40602 | -59.59073 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abfaf764-2b3f-34ca-917a-00854d0d741d | -3.55003 | -59.44517 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e3671a4c-0a29-381b-bada-391e3eb6112a | -3.53481 | -59.41278 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ce4800-6d92-368b-a777-ef3993838f50 | -4.77518 | -55.73519 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 52145792-6030-3419-b7e7-029ba4acaff2 | -7.75491 | -54.95762 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e45ed3bf-ecf6-37d1-a93c-ab780aebc506 | -2.77457 | -54.07588 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ecd3f14b-062a-3ee2-aa4f-ba9ab0dc693c | -3.33273 | -58.17144 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 139b96dd-c8fc-3a1f-affb-1668d3005dba | -3.18058 | -50.57003 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c611892-24e5-3186-9724-562aa82f8c96 | -6.11756 | -55.78372 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec18e7a1-c12f-3642-8e27-32d0530ff5af | -2.5044 | -56.18472 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c0f91a2-95c7-343e-ad70-64aa17355928 | -3.25812 | -54.67767 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d58fffc-f3d9-3e62-92bc-303f9d16ffa3 | -3.00338 | -54.12509 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f284995-fdc7-390a-ac2f-b0326fe725cf | -3.51672 | -54.66624 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 560e8e78-5d84-3787-963a-249b0579393c | -3.00387 | -54.12182 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf77cc70-9a2f-3f6d-ab77-dd9f75d104f5 | -4.93643 | -55.81031 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c8067fd-7e52-3d19-a137-fcb5f120d1b1 | -3.02007 | -54.05013 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed9d1c6-310f-3e67-b7a2-5e436ede9e15 | -3.54061 | -54.62677 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8aa6cd-140d-309b-a187-607dad980a8e | -3.30785 | -53.86821 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79647e76-2e7a-3cb7-b847-6af3f3012e51 | -3.03178 | -53.93563 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ec3a06-2996-3f67-abae-344ccb7dfaaa | -3.26761 | -54.012 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa66034-8ab6-3262-8965-4ca443ec18d4 | -3.89733 | -59.45037 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22dd6c94-ff93-3d85-81d7-e11fb6548c5b | -3.86577 | -56.00571 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d24df34c-4344-35a6-b5a6-e95b30add548 | -2.76157 | -54.09052 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52bf60ee-0f53-3e11-88e7-ba922f3df0eb | -3.09769 | -54.28208 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a28c19d-2d22-38d4-b85c-23b52473c802 | -3.84774 | -58.89718 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56a48711-d0f4-3cc3-9fcc-186536ed955b | -5.29283 | -60.10318 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99fe7b8-6b38-317c-9cae-06d08783a0fd | -2.79908 | -54.0929 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 287420ff-ba18-33c7-9074-43879f77c54c | -3.29535 | -54.02985 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24bd4a94-70a9-3ed4-bcfc-f3907d6e42ab | -3.19024 | -50.57552 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f66a436a-64b9-3d1f-9625-27823b53caf4 | -3.28288 | -54.05546 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d0915f-3bc3-380c-922f-4c603e171529 | -3.1714 | -54.6111 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b700670b-c9f7-3bf7-b54e-de0d7422315a | -3.03482 | -53.91532 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57e3a1d9-0dd3-3373-86e1-be3ad6bcb856 | -3.3069 | -54.70093 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97bdd17f-be08-3235-a1ff-5d4b4d722fe2 | -3.03613 | -53.9432 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 371c5151-d4e5-3143-88e4-fe2762214ff7 | -4.09306 | -52.0643 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 781f7b53-2092-32f9-8986-3925cf29fea2 | -2.79477 | -54.08556 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c78ee1f-efa2-35e4-9ccc-1f1aa7dc6228 | -5.70273 | -53.50225 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87b38861-4674-3611-8519-79a91439224b | -3.3021 | -54.05841 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdbb5b4e-a13e-33e7-9549-b484d5b76ed3 | -2.9022 | -59.22341 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e13865-e17e-32c1-998b-e0d43b3b2ede | -5.24509 | -50.91679 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dbdc223-2047-363b-9f3d-2f9c8edce707 | -4.12047 | -59.87869 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ced21ff7-31de-3d84-97c1-626c73577055 | -3.08444 | -53.95025 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00e06e3b-a868-3a27-88ab-103eb628b9ac | -3.86062 | -55.99797 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 192b55f3-bd23-3902-8821-29845647c852 | -7.18598 | -52.61412 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bcf97d2-ef86-370b-bc88-3c3ad92e6ba0 | -3.08948 | -58.01933 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a022b2-8de9-3cbd-aff7-537115c4f522 | -3.97061 | -56.12381 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee4c2f65-11f3-3267-a97c-bf1c3816cafc | -4.16059 | -55.14305 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03f8a41f-23a1-3db2-a60f-3425d0bf08fd | -2.48733 | -56.14392 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bce5823c-96d7-34e2-9848-93ced3d7c3e9 | -6.24075 | -52.85872 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09248abc-2d9e-3803-ba4d-36b7dd9208fa | -2.9976 | -54.12753 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bb06340-d5c2-3f8c-9857-3737e1924486 | -4.7662 | -55.72839 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90779d9d-5649-38e6-a587-f69265ef0952 | -4.11019 | -55.17161 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7032739a-aba5-3b29-91b9-a5752b1020d5 | -2.69558 | -56.5399 | 2026-10-08 05:42:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f543589c-d401-3319-b8d0-877ab98ccf43 | -6.10167 | -55.71809 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93176d26-8124-307a-90af-95d6f5508a58 | -3.19277 | -50.5582 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0187ff48-a05c-3236-9bef-54b02a3f20c7 | -5.73896 | -53.45934 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3c0221-f366-3cb4-a649-10bd298a4e3c | -3.08771 | -53.96463 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| df2d5050-f06f-32b6-8eeb-122297599cd4 | -5.29776 | -60.10088 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d8ae2bc-987b-3004-92a0-cb270f5c6e9f | -3.96053 | -56.12726 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 042a1176-2105-34f3-aa33-7fcdf0a94fba | -2.57639 | -56.17436 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe84a00e-57e6-3c46-a453-3c964f0827a9 | -3.11119 | -53.77597 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bcb4d83-bc13-32f6-82d1-361e05a6c9f3 | -3.20611 | -50.56018 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 65a45f31-8e3e-318c-ac67-3e4fb3a43a7d | -3.00211 | -54.06102 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33d9fd6c-8209-3fd8-b8cc-53b07a87ba5f | -3.30498 | -53.87485 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e24a97-d79a-3666-af7b-b80f3012709c | -3.56595 | -54.49 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47943f48-b93f-312c-92fb-ddb74c49cb04 | -3.51157 | -59.21363 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 457b2131-a428-32a2-bdd2-d99c33817cc0 | -3.29758 | -61.01651 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb0ae9f6-b6bb-3287-b7f6-1786bc8edfac | -2.97553 | -54.13037 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bdaa7da-f2a8-3e33-9db6-eeda57a749fd | -3.27068 | -54.06379 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8d156f-df57-3466-a20b-38be59dd6763 | -3.57727 | -54.66385 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bee2af62-cbe3-3b0b-984f-2dea477d6f9c | -2.498 | -58.07719 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7b426c4-c923-3b58-9093-31e1b5cfa6ce | -3.57963 | -58.5534 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be82ee9f-c7bd-3dee-92e5-f321fa960dd8 | -3.22399 | -54.29964 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8813c141-f54a-3166-b540-01f478341e14 | -3.301 | -54.0443 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 268ff579-b260-3457-b36c-3a1892f20198 | -6.47719 | -55.30475 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41c68e3-30da-339f-8a94-356681341954 | -3.04584 | -53.95156 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8d029e95-228b-3bbb-81a3-0ddc513299f3 | -3.29341 | -54.00555 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5eab46c2-298f-390d-ad95-4a7fd582171b | -2.15744 | -59.22751 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 52fc97ae-f198-30ca-b0ed-da219afcb6fc | -3.29892 | -54.05774 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9fc8fc9-244d-3928-a562-3ed3d85e1464 | -6.14986 | -52.64866 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README177.md)
