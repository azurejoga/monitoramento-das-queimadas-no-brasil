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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2807010-da02-362e-8049-ea572ca4673d | -4.47735 | -55.08962 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03b3d5f5-ef49-35f0-b331-3589958e14ef | -4.47371 | -55.08905 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95d0039d-1dba-3967-9cd3-66f9431f699d | -4.47305 | -55.09331 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 128c55f3-ef9c-36db-b1a7-cafe71c94bc4 | -4.46249 | -55.11349 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b236ce1c-fa12-3460-aca0-594c1d5812fc | -4.45885 | -55.11291 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a5d3375-7438-3259-9e1f-797a3d8b03e6 | -4.37152 | -55.32184 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9cb410d7-439f-3942-a459-8415528be28d | -4.33328 | -55.19868 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0c53b05-b050-327a-b4b6-f23671b509f0 | -4.3321 | -55.06034 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e16358e2-374e-361a-9a92-8816ed0ddb70 | -4.32845 | -55.05979 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb3b4e0-76d8-3c25-a82c-7c21e168bfa6 | -4.30569 | -55.08706 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3da2590d-7f7f-387b-bd0e-cea1814da4b7 | -4.30506 | -55.09122 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49cd6c19-e408-34a0-854a-baf7b44e90be | -4.30205 | -55.08653 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c22e7f76-6c12-36b9-bed8-c02f7aa8f084 | -4.29477 | -55.0854 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 169e6f8d-202e-35e1-a212-777621b6c5ca | -4.2927 | -55.12389 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61f3a998-e745-3e70-b3cf-cce7552de353 | -4.27232 | -55.18545 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4577e65-24fa-3e80-a0dd-82ef860867ea | -4.26112 | -55.15461 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5e82dea-8f5e-3a1a-8316-1fdd2a9962f0 | -4.25751 | -55.15392 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e826410-dec5-3323-afd1-937ae541b22f | -4.10066 | -53.93136 | 2024-10-27 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4da76a99-b149-30ce-a8c9-0638ce2c0912 | -4.01674 | -54.81877 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 752d11ac-7cd3-373e-89cb-4313b5c4875e | -4.01608 | -54.82312 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2477861e-d93c-34f6-99ba-a84305170241 | -4.01306 | -54.81818 | 2024-10-27 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d02b7c18-8294-3582-9b04-a18b814ed03b | -3.66964 | -54.21394 | 2024-10-27 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 21b2271a-dd00-320c-9d94-6b32a91e8ffc | 1.59888 | -55.6702 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8373f173-92fc-3c29-a6bb-87755b5a9d3f | -2.06005 | -55.69748 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04523b92-2afb-34dc-96ba-587842bc80d5 | -2.01523 | -56.05323 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06fe02e5-d362-3965-8523-927a48c43c78 | -2.00692 | -56.3721 | 2024-10-27 05:16:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6504bd4-c989-3d1f-bbd0-048c29b9316a | -1.98551 | -56.46436 | 2024-10-27 05:16:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f5a89a7-b9c2-3cbe-87ce-781460673551 | -1.96354 | -56.02639 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a53c55ec-c836-3bb1-a21e-efe4e59ecd11 | -1.96297 | -56.03008 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5fcb0e16-ec98-3157-bf69-6698c52da1e8 | -1.96013 | -56.02586 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb430f4f-b780-3114-9aba-8ab42142440d | -1.95956 | -56.02954 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf2036c-20a4-3390-8eae-5dd95e06b611 | -1.83444 | -55.74898 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1acf52e2-978c-3483-87e5-17ebc12a8b01 | -1.72537 | -55.0037 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c46f043-e3ae-3140-a798-a60695ba9c8f | -1.72182 | -55.00317 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 994432aa-fdf1-35e6-93ce-dc143fa94543 | -1.68177 | -55.3084 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e272a1-462a-3695-a555-84db74118946 | -1.64453 | -55.19558 | 2024-10-27 05:16:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12ab83fc-41fd-383e-95f3-b9e8a500acf8 | -1.60636 | -55.70315 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 094f1600-1f93-3c96-a9c6-1893dc8998f7 | -1.60292 | -55.70261 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b2d8c02-65a4-322f-9575-2e2ec229d924 | -1.60235 | -55.70635 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cad22bf9-a007-3a39-8574-259ecc054817 | -1.56556 | -55.89863 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f32fbead-d0d8-3952-86aa-c28f944fd2c9 | -1.56499 | -55.90232 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a2f5459-e8e4-3d70-8da1-a417ccf014bd | -1.50302 | -55.91589 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed177d4-a24b-3940-9aa8-1c795d6e7fc3 | -1.50244 | -55.91958 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eea849c-99a5-3fae-badd-a5068b5f66b5 | -1.48405 | -56.05917 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d044f7-cdaa-35e1-a5c8-b9ca800eafde | -1.42436 | -55.07435 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f651b10a-03d3-3358-843b-8b0f82497a52 | -1.42374 | -55.07832 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65f410ee-3541-306a-bc17-5c6e40546f33 | -1.42293 | -55.32124 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 008928c5-6a9e-3004-948a-3c21f4260b2c | -1.38712 | -55.19736 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20f8634d-614c-3bba-8991-33a05609b6bc | -1.37514 | -55.85841 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84a046a2-2635-3891-9077-6185e6222ae1 | -1.37457 | -55.8621 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84f9a957-d13b-3520-be57-9b882248719f | -1.3743 | -55.39347 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b9e2ba7-0e6d-37a9-a4d7-77e147817ea3 | -1.3737 | -55.39729 | 2024-10-27 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 380093f2-96ea-3e20-88bc-0b58485dd549 | -1.37173 | -55.85787 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7db5005e-1fde-3631-b3db-c531be159d98 | -1.37116 | -55.86156 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4deefb3a-2eb8-3431-a5f7-63461bed440a | -1.34101 | -55.87571 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fac5cbd-7014-3fa5-8e43-95f82730cae0 | -1.34044 | -55.87939 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f78eb21-4097-3d8c-b535-12a05b73fd11 | -1.33817 | -55.8715 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98afa066-a2fd-3a5d-ba46-c931af7f0ab0 | -1.3376 | -55.87518 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae7971a7-341c-3f9c-b397-b2bf284af64e | -1.32909 | -55.9753 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81a9b779-3e58-3fa0-b0ca-6ff19806cc41 | -1.29192 | -55.71696 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5343ddd3-2e6d-3a0a-a2e2-099c3da1ca65 | -1.29134 | -55.72067 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 220876d9-c866-3446-b40d-3f8be9d36a07 | -1.29076 | -55.72438 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faf7f411-4954-3c0c-b6db-8ad048dd15e4 | -1.28907 | -55.71272 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef30bfc-09ec-375b-a83b-eb5f0839adba | -1.28849 | -55.71644 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10564d63-d22a-389d-8f17-dd3d069b4beb | -1.28506 | -55.7159 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8961ee5-ec93-33d5-aabf-d4a2c05b3f84 | -1.25701 | -55.76108 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0940d0dd-51ca-3f5b-ad17-ea0d7dcb8a7e | -1.24678 | -55.69096 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60132f88-fca3-3681-bbc5-6f5ec63bbb2d | -1.24665 | -55.69165 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1880b49d-866b-3c73-8373-e912831bf184 | -1.19912 | -55.92626 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbadff6a-53ba-3c35-b26d-fb636c4a4a17 | -1.19854 | -55.92994 | 2024-10-27 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e33b42eb-4020-35c3-92f5-5b7ff5571cd3 | -3.01834 | -56.62239 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50f9d26e-5f32-383a-b58e-a9381f85dd03 | -2.48218 | -56.05217 | 2024-10-27 05:16:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27e11346-864d-3624-8989-9eadb644cf28 | -3.63275 | -55.51241 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3919070b-bc3c-3220-93f9-9445e2150875 | -3.62983 | -55.50792 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a694b07-ea7d-3797-8205-351c30619d6e | -3.62921 | -55.51189 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 983b844b-fb8f-3f1d-986b-4cd7e62d34ee | -3.62629 | -55.50737 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 056d03e2-b14e-3003-9b31-019650c2d94e | -3.62568 | -55.51134 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e5d4557-4e07-397a-b792-d206321ad3a8 | -3.56732 | -55.5144 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84a9c5c-1be8-380a-9a66-255f50e14ecd | -3.55525 | -55.45183 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d5a60cb-ba96-35c5-9ac5-4f550d21b14c | -4.58227 | -56.10561 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5962b844-fdb3-34e8-8aec-81ae6c018833 | -4.491 | -56.10831 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acb8a981-e6b8-3174-8a24-e0c72591a0a8 | -4.41774 | -55.92304 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a85e628a-8deb-360b-8a81-d2b49e19d800 | -4.41714 | -55.92694 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d593aa-eb9d-3d65-99da-f85e15322ae7 | -4.34317 | -55.74782 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a59502d8-63b0-3e71-b231-7e8b90075755 | -4.32152 | -55.72421 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e781907-1240-3f1f-a8f8-ae7173af7024 | -4.2784 | -55.74315 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d483b0-5cfe-3c9e-91b5-c697877bbdfe | -4.06862 | -55.83992 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7de32ce-748e-3cb5-907a-89aec225f837 | -4.01087 | -56.26553 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a4f3e5e-5206-3aea-9c50-01cca2f1ca9e | -4.01029 | -56.26926 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 511faec9-3cd9-3056-8581-d40723306844 | -3.92002 | -55.92663 | 2024-10-27 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554892ac-f50e-3219-a73a-83e4207261e3 | -3.81381 | -55.88684 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 626da139-982d-3f35-ae69-42a8464b407c | -3.70007 | -55.96449 | 2024-10-27 05:16:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c49cb13-18dd-32d4-afb4-b4a7936fc302 | 0.6784 | -56.87274 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80e380ac-b6d3-3163-911c-b7cbfcc50ca4 | 0.67786 | -56.86931 | 2024-10-27 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3239ca2d-7805-385e-b721-2754af66d821 | -2.10932 | -56.66933 | 2024-10-27 05:16:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98411f89-8306-3f33-ada8-4aa519ae2b97 | -2.1074 | -56.54892 | 2024-10-27 05:16:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05341ef2-1e18-3577-9879-7344f5b97a40 | -2.06082 | -56.87123 | 2024-10-27 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bfc195a-df06-3d0c-a2ba-d6cb92b3a110 | -2.05803 | -56.86722 | 2024-10-27 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f09700f-786c-3db4-849c-f268e1137f7d | -2.05749 | -56.87072 | 2024-10-27 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd950b8f-a089-3ed7-86d5-a315b88a0d6c | -2.0547 | -56.86671 | 2024-10-27 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README62.md)
