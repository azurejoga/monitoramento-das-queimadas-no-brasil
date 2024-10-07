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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb17af6c-8703-3750-b2db-8a41f60f2fb5 | -19.13861 | -42.72847 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3dc9ab19-8b81-34f4-a269-63d5dd0004c6 | -19.13804 | -42.7321 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 089c106a-17eb-3627-b68f-fca694d4a42a | -19.13747 | -42.73573 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 815ff11e-5c57-3632-b569-10d078a86576 | -19.13633 | -42.743 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bba2937a-984f-3c69-9359-69ec65024bfb | -19.1353 | -42.72789 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1d9253c5-7f96-351b-a847-82b3225834dd | -19.13473 | -42.73153 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| af52249f-3690-30ed-8d61-12b349935748 | -19.13416 | -42.73516 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0d63d3e3-e545-3c5b-b707-6e9de31ed8aa | -19.13405 | -42.75756 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| da034684-98c6-3446-9376-3281633afce7 | -19.13359 | -42.7388 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e39042d1-d733-367b-9111-51ace9cd238d | -19.13142 | -42.73095 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d90f57d6-4b9b-3e85-874b-32257a2a8d6b | -19.13131 | -42.75335 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 55e86077-5f31-3406-9d9f-ee8054ea9709 | -19.13085 | -42.73458 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 55fc8824-f2e0-3a72-ba05-03222e0caf97 | -19.13074 | -42.75699 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09b9bb8f-8f51-3fa6-af13-bbb3395277b0 | -19.13028 | -42.73822 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| db645517-35ad-3abf-a008-0b73ce4b8f4c | -19.12813 | -42.73039 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a35eed96-451d-3f4e-93bc-eb164e0639f7 | -19.12756 | -42.73403 | 2024-10-07 04:02:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d0ddaf59-9d4d-3ebc-911a-2e019aeecb49 | -19.0699 | -42.5372 | 2024-10-07 04:02:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7977f82-d12d-3e3a-bec8-59880f52ff00 | -19.06877 | -42.54448 | 2024-10-07 04:02:00 | NOAA-20 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4880f03c-76ee-3e67-b1a4-b4139fabc957 | -19.75492 | -43.02068 | 2024-10-07 04:02:00 | NOAA-20 | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 86890534-b17f-3a29-803b-12e1a2c584ce | -19.66317 | -43.19286 | 2024-10-07 04:02:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4c4477c-fa7f-345c-999f-92f8c248a8b9 | -20.45309 | -42.3704 | 2024-10-07 04:02:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b9425528-145b-3665-b27c-f07f04e3b9ce | -20.25968 | -42.92024 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dcc98709-7a6c-3127-acbe-d8518523dbbd | -20.25911 | -42.92391 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bbc70849-982a-30ab-9a41-6415c78799ff | -20.25853 | -42.92758 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 41e81b04-b530-307e-a198-4f84385bad6e | -20.25637 | -42.91967 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0f27574e-f51c-3ed2-afd7-caf0c3d5e605 | -20.21345 | -42.88955 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 51efae96-c728-3176-a35d-4e96ddfc7ed9 | -20.21288 | -42.89323 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99a02ebb-4858-3a21-bb58-71f639c10767 | -20.21231 | -42.8969 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d84651f1-e685-3531-aad3-2366d89d56de | -20.20957 | -42.89265 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e4bf953e-c1a6-306c-8bdc-000dfaacfd2c | -20.20797 | -42.88104 | 2024-10-07 04:02:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ff028e1d-0db5-3654-9a0b-842f25db1038 | -19.97828 | -42.45712 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| b74faf1d-7fc1-3182-9ec9-eb9fc7ae6468 | -19.97772 | -42.46078 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| 1112937f-88ad-3993-83e8-f6fa4eefb2c3 | -19.97496 | -42.45654 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| a2bfab40-edce-3ce1-a6e9-d3974445b948 | -19.9744 | -42.46022 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.7 |
| e726835a-7c4c-3e9b-8aef-4ed2fb27d47e | -19.97164 | -42.45597 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a83e162a-e838-38d6-9154-9bb85890f245 | -19.97108 | -42.45964 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2edad3b5-e60a-3958-a1e3-48fbc4395c24 | -19.96832 | -42.4554 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8f931177-8c7c-3898-b85f-daf67cc2ed0f | -19.96776 | -42.45908 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29aad778-98ce-308b-aaf9-d81d6d42fea0 | -19.95999 | -42.46529 | 2024-10-07 04:02:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 4255f8c3-2bce-340e-957f-3d23856e522f | -19.84776 | -42.3787 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 0a0669d1-0c08-3e57-b4ea-a8a0516ee858 | -19.84772 | -42.40118 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ed4e9f63-0537-343d-9468-848f7702e4a3 | -19.8472 | -42.38234 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| af05c460-c801-3f9b-acbf-0f20b697d98e | -19.84715 | -42.40485 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 91f8700e-c24e-366f-9279-b1b45270bf47 | -19.84659 | -42.40852 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c16fe99-5406-3f5d-a566-1fd0772857ff | -19.84444 | -42.37814 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 71d4d121-2c05-3032-b6e1-bf10931987a7 | -19.84388 | -42.38177 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7cdb109e-9224-35ef-b547-8aefe30eb9ff | -19.84383 | -42.40428 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d3fa03a5-42f1-3223-947b-c68890a81af8 | -19.84332 | -42.3854 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 6dbd329c-5072-37f9-8856-8ae7312146c4 | -19.84327 | -42.40795 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0a7ca27-ec6d-3f18-8001-639ff01a4bac | -19.84056 | -42.38118 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 5b7a9f9f-e3d2-3fcc-af93-7fa00c1966a4 | -19.83529 | -42.37361 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1dd56569-6323-3ad4-8e48-654e365c21e0 | -19.83474 | -42.37724 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 90ead605-caeb-3a73-8b99-58bda760af63 | -19.83197 | -42.37305 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a2cf27e-effe-3758-8489-c8a261bd0b88 | -19.83142 | -42.37669 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0def2691-45f7-3b30-b3d3-944260b71b31 | -19.83086 | -42.38033 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2213c810-4201-3d75-8d0d-a1d6ab9e83fc | -19.82977 | -42.36517 | 2024-10-07 04:02:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fd7a0872-c101-34c5-ae4b-3893fd3a2119 | -19.82921 | -42.36882 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b16a9900-3aea-37c7-9893-9a1abec495a8 | -19.82865 | -42.37247 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2e0b51a7-da23-30e0-b1cf-311eb432b7fc | -19.82646 | -42.36458 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6bd02449-6d08-3eb8-885d-4c7af071f968 | -19.8259 | -42.36823 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d159c80a-3582-3480-a85e-71f3d8484870 | -19.82534 | -42.37187 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 399eed89-a901-3f3a-b3ba-4f1c12e9609c | -19.82478 | -42.37552 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db25c098-2af6-34b6-8ffc-c0740418a1a1 | -19.82422 | -42.37917 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 579386ab-ef9f-324b-9669-9833bba994c8 | -19.82371 | -42.36032 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e8770d9-4799-35fb-9512-f8831c3b5d86 | -19.82314 | -42.36399 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a20c4ff-6318-314a-a955-493999f7ed04 | -19.82259 | -42.36762 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b2f10588-46d6-3792-8caa-02afd4dbc48b | -19.82147 | -42.37492 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e134266-b4a9-3ea7-bed9-1345eaa92f4f | -19.82039 | -42.35975 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| baf8b9f6-7992-3692-bfd6-f898905a8f31 | -19.81983 | -42.3634 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b2b0de84-a5b7-384b-b37d-4ab13ad191d5 | -19.81927 | -42.36703 | 2024-10-07 04:02:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c27dc47c-16f2-3404-91b6-b749ac397212 | -19.77771 | -41.9967 | 2024-10-07 04:02:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 88ee00d3-3283-3b56-9280-ddd7898a9975 | -19.77715 | -42.0004 | 2024-10-07 04:02:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b2a9a3b4-abc8-31cf-9d14-cc7bdafe06a1 | -19.77438 | -41.9961 | 2024-10-07 04:02:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5aa8938a-e2e2-3d86-a444-654b2aabfaeb | -19.77382 | -41.99982 | 2024-10-07 04:02:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a20e9b63-e577-327f-b780-f9590ff754a1 | -19.71805 | -42.09671 | 2024-10-07 04:02:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9c67e1e-dd9a-365d-90ce-5a45e00dea45 | -19.89551 | -42.64317 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 38a0c5d0-8623-3f6e-b9fe-aeca2e583690 | -19.89495 | -42.64684 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 5f0aeada-7d8a-3817-a18a-a52571d3ce5c | -19.89438 | -42.65049 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 7eac9264-0c12-33c6-8e3d-d90d2bda7cd0 | -19.89381 | -42.65416 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| f6bc3090-2f95-30b4-9702-2ca8df90d56f | -19.89334 | -42.63526 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| be6098c4-5b96-33a5-9552-8e73b1efd6f3 | -19.89324 | -42.65782 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| e14342d1-4f81-3bd9-9826-1d132da1da8f | -19.89277 | -42.63893 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1d09ad99-9c0d-32a3-9fb3-bdbcbb4bf857 | -19.8922 | -42.64259 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a0831923-0971-351d-ae3a-bff9b7bdadd5 | -19.89163 | -42.64626 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 30d9ab66-983d-3381-9ee2-053704bf94ad | -19.89106 | -42.64993 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 3d6db3a9-7952-3d0f-ac5f-416998c25c1f | -19.89049 | -42.65359 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 37bf7865-96a0-3d80-b6d3-25e087b946c2 | -19.89002 | -42.63468 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0c4ba961-7245-3d55-84a6-d23deedd15e3 | -19.88992 | -42.65726 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| de4cc33c-39ca-3451-9c26-d16f86820fa7 | -19.88946 | -42.63836 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 10fc6786-7f03-3613-bd83-018a31ea1d70 | -19.88832 | -42.64568 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 66e0922d-287f-3bf6-ad6b-28310dc8ef3c | -19.88775 | -42.64935 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 99b18312-a0de-339d-b7a3-839fe4e86c65 | -19.88717 | -42.65302 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8e25a20a-55f2-33c3-aa8a-94d4613591e7 | -19.88661 | -42.65669 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 051f7680-a51c-3c60-8ebe-18644955e19d | -19.88557 | -42.64145 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ed75cbd-7843-363f-b1dd-894a66a404c1 | -19.88443 | -42.64878 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f40642bd-f08d-31c1-9404-e65a652119e9 | -19.88386 | -42.65245 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7e325ee2-891e-3566-a54b-a4ba95121d8e | -19.8834 | -42.63353 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 97512016-8c39-3a1a-b87a-0eb7b2c6756b | -19.88329 | -42.65611 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| be57abfd-2c71-3037-8093-9c298ef5f448 | -19.88226 | -42.64087 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 95a39085-959f-3d89-a9e1-ef4ba84da979 | -19.88169 | -42.64454 | 2024-10-07 04:02:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README66.md)
