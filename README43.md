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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12b6ee67-0d11-31e5-9a9e-7ff869a128fd | -4.11974 | -48.48763 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88f6f070-15e5-3e11-96c3-2bccdc4b022e | -2.02669 | -52.07833 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a4a9781-3ed2-37ff-806a-cf48972e193f | -4.19497 | -50.68229 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c832c9a3-852a-3d62-9c02-ba4d3a933217 | -4.01322 | -49.9417 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c6b7bd1-2889-3dff-8119-4755217776ba | -3.85207 | -54.2208 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55168c51-012d-3498-8d3e-937e1206121f | -2.00755 | -51.17983 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf2fb955-674d-3769-86dd-31e49c7741f9 | -1.73144 | -46.65832 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 282257dd-5845-3946-a2c8-915ea579e54f | -2.71262 | -48.6546 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc7f6f2-afaa-3f1e-bc02-2465943f7b6e | -3.19695 | -46.58142 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e55aee39-3ce6-3a9b-911d-15ba4f4638b0 | -3.24669 | -53.92462 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14099062-d1f3-3bcd-839a-9f8c33976efb | -4.04507 | -46.83136 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86392cc9-85c4-31b8-ad48-a095bb34f447 | -6.30405 | -43.84544 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e76dc9f-d5b3-3e4e-a197-57e333855a32 | -1.19973 | -51.74181 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ea7651b-d349-34a3-a42e-e065683d85f8 | -3.21664 | -54.23132 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e5d2e7-dc68-3b21-ab40-ad9bbfc9c97c | -3.27722 | -50.53455 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cc22fa8-6c5e-3011-b115-b2430e296ffb | -4.43361 | -48.69447 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc5691e9-6be5-302b-8548-9ea0e163b26c | -4.00516 | -44.75656 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| e138649d-322c-3c0e-af9f-6745dd089db3 | -3.85148 | -40.98142 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f800fb29-7635-386a-9b38-ee61cfff1d84 | -1.67399 | -52.09788 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fe1f3448-ad65-36aa-b5c9-8dddbe1b0412 | -3.3837 | -49.85797 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af7588fb-1438-37a2-974f-1959371cf0f1 | -3.50288 | -50.32632 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63ca9040-0728-301f-9303-097eb2f19b6e | -1.70301 | -52.46454 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 726af883-1271-3372-8421-ac1638fa20e3 | -2.16865 | -50.91249 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e916ddc7-c8eb-3ad7-8901-f91a6f2fabd9 | -4.54115 | -45.70402 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 96fd4fd7-a14b-310b-a599-126f8ddff67c | -3.22804 | -51.50418 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44fa232f-12e9-3946-9d7c-eeee40accaca | -4.76654 | -49.49567 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21d06fd9-d02a-3cf4-8f69-063396b08024 | -2.28576 | -45.60335 | 2024-12-01 04:44:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6d0ebd59-74f6-305a-8695-bdeaea772675 | -3.24443 | -53.62997 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0657cc1-5872-3388-b1de-c27020ef580c | -1.08443 | -53.63749 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01f365a0-ec0b-344d-b8f3-c835acaf9295 | -3.33968 | -53.28954 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e3da09-53b0-3e32-8c8d-b676214a407b | -4.09047 | -46.13282 | 2024-12-01 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 997874b9-0997-3497-92df-6737a79b2adc | -2.36491 | -53.86326 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a056783a-42bc-36a8-8bd3-b4f94f818b21 | -3.75449 | -52.2738 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 016e6d55-713c-3107-9f08-9d69c0e5563d | -2.74805 | -51.75341 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9f391b8f-e422-3016-a6df-6e972c686ef0 | -1.72395 | -52.49192 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7026b1d-7c7c-3b67-a300-0a1f281ba163 | -6.92637 | -43.54829 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ecca7faf-e9e1-36ab-8073-78c754e6e104 | -2.5892 | -53.9804 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f67f62e-cafe-383a-bbfc-cd3f903b3cb9 | -1.04957 | -51.73784 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38e3d52f-8915-3b8a-aeb8-3024c98e3410 | -3.2497 | -53.92976 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88aa4aa5-7f8d-354d-b1a4-0e193bf9fab4 | -3.53474 | -62.77558 | 2024-12-01 04:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88712a67-beab-3c6a-8a80-fe66962fc5e9 | -2.99924 | -53.36583 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffe33009-c77d-372b-b228-836f4b863094 | -4.7699 | -49.49619 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75676359-76f8-39a0-9258-5d0202f587de | -6.2893 | -43.84858 | 2024-12-01 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 319a3db7-43ac-36ff-beee-06e376388c48 | -2.36424 | -50.42305 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb4106c4-1182-31d9-977e-59b4476a535e | -2.1009 | -50.74092 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbe03600-9a8f-3843-8b8b-be31d3e32edf | -3.75603 | -49.94451 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87c7bfa4-7145-3f1d-81f0-5b01052cfab5 | -3.24747 | -50.59362 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1507471-af49-3aeb-aa9b-46749314e331 | -3.15386 | -50.62856 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f6f0a9f-4924-346f-b7f3-376b7e34be0a | -3.01247 | -54.0861 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6105f269-65b7-34c9-b695-6f215a059698 | -3.26296 | -48.7714 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3a22b42-2b2e-3cd5-897e-4239ca4d60d0 | -3.76879 | -51.61776 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9452d48-3462-3088-8ab0-bc9d3f4aed54 | -3.03056 | -51.53576 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54e09bd1-89d7-3216-aacd-519b46c799e0 | -1.65898 | -52.40166 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4df59220-c3b8-34c8-8e25-d31872e0ca23 | -1.4216 | -54.31199 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50f65a5f-23d1-3e85-879b-948248d60c07 | -2.81147 | -54.03923 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e6ceae12-9f55-38a6-9457-8b97ea838b99 | -1.45382 | -51.502 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77510163-4925-3c92-9430-fbe5185b3d91 | -2.37469 | -50.39991 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cd641d5-e3f2-3ca6-9087-a342314fa076 | -4.49307 | -48.21415 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| beb7e9ec-eebf-33d3-80f2-1f68f99e012e | -3.85106 | -40.97842 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 750edeed-9ddb-36db-9345-d5bae472020b | -3.21357 | -54.17904 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc5e559-bc16-3cdb-817b-e41724806e8c | -3.07243 | -53.81298 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54e4a038-6ac6-3f67-a99b-9004bea0c1a8 | -2.48585 | -54.0229 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b68d98c-b7da-377d-808e-a882317978a9 | -3.05968 | -51.0592 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31b651d9-868c-3a4b-85ae-2b396327c5cd | -4.26764 | -50.84229 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b0de6d-ef2a-344f-8c33-7d63384c0734 | -2.11956 | -46.56025 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ca03f9e-ef10-3d1c-985e-6f4db8acbae6 | -2.76865 | -51.68984 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b318246-72a1-3789-8342-26edb217f6b0 | -3.65862 | -50.71133 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb74554c-1be7-3888-afbb-686e154e8d83 | -2.63534 | -54.20001 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 397356c2-68f5-3977-971a-65c16b993c7e | -6.9271 | -43.54308 | 2024-12-01 04:44:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5105b3ea-ea58-3b2e-bdad-65f1ab705b6b | -2.14285 | -50.62633 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40f8a89c-b3b0-36d3-a1f5-d79b6563ec60 | -4.54122 | -45.69733 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf614f9-d4b4-3488-8a65-0a85b88c7f1f | -3.75192 | -50.05725 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e276e0b6-8455-3f0b-8150-aa40693921ef | -2.59526 | -53.99064 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f097fec0-cfd8-36b8-83c4-76b4ffb60680 | -3.06193 | -54.04311 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b090ae2-663b-3eae-a6b5-b863fb4a3e51 | -1.27289 | -51.82892 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc3a8159-e036-3d5a-8fde-bee37f49f819 | -2.7947 | -51.89922 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b0d337a-ce63-390b-bfd5-f05f9decabe5 | -2.90385 | -54.01685 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cb2bec3-ccff-3fae-922e-f201740ef0d6 | -1.44431 | -47.11539 | 2024-12-01 04:44:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6128e21-4963-38da-9d8d-d47149716d15 | -3.70929 | -53.40699 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b53a29a9-6895-36e8-9b56-68084eab13ea | -2.69402 | -46.86581 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b99f2a8-8b6a-39de-bf03-ab751aaa17b6 | -2.45575 | -53.70658 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff7e666b-de7b-3edf-8658-8f1352e5bd69 | -3.02308 | -54.02072 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d54d544d-ac07-31a9-8c94-2f8441fe995c | -3.05673 | -54.05143 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba95d543-1c6d-3d11-bfd4-933babca971a | -2.80173 | -49.77434 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b88ef709-5a1f-3f26-9fae-c9a3f2dfaaad | -3.21432 | -54.17446 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97aec359-7bc8-325e-836e-15ea40c997b4 | -3.11253 | -53.99129 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eb598d6-47af-3ae8-8881-5b590eb352be | -1.63135 | -53.86372 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ade0a2e-8a4e-3179-b4a2-4ad7fafdeba4 | -3.05744 | -51.05167 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cd3fc32-6d6f-3048-9715-6431caefd3a8 | -2.88703 | -53.97723 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de1a8f9a-a76c-3c84-92a7-78eb6c5fec99 | -2.84496 | -49.88351 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2c3599a2-6101-3cbe-9824-556f95256d48 | -2.57469 | -53.97588 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696cbf9d-09c7-3548-9a9d-bacbf9b3c77e | -6.76173 | -46.53091 | 2024-12-01 04:44:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89171896-e875-3bc2-ae74-84e8ecdf14e4 | -4.00034 | -44.75981 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 733a0f2c-1b1b-3f4c-92b7-caa3f39a3a8f | -2.88273 | -54.00422 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2799d497-44ef-3deb-aac9-2428b0ce1dec | -2.84245 | -52.53627 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19cb722e-40c5-3b95-b75e-85be6a8faea6 | -4.35506 | -48.70548 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfc96584-6aa8-30b8-9aca-89e80526ac5a | -3.21877 | -53.62598 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5de9421-7751-378e-9bb4-18caa2e3769b | -2.46832 | -50.36505 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07eaa426-d210-31aa-9cd9-8112065e5ea1 | -3.6783 | -50.24395 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9048dd07-c23a-3b36-93f5-2fcba044b611 | -2.78504 | -52.98268 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README44.md)
