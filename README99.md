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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03e49fbc-68cd-3ed3-a55b-3d482a1a8ce8 | -11.0461 | -46.9842 | 2025-09-01 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6c274acf-d4fa-35cb-a84b-fed7456bb029 | -15.5862 | -48.3435 | 2025-09-01 08:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 279a2078-9313-3d1f-a338-763357f298ba | -12.9194 | -56.9672 | 2025-09-01 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 3442470d-ae9c-37c5-9a58-c4cff3613230 | -15.7116 | -48.8809 | 2025-09-01 08:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 22504131-9918-3a3d-b3ed-98ce8717fda4 | -12.9387 | -56.9454 | 2025-09-01 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 6aa7c209-9f0c-337a-a273-aae1600aca3d | -12.9385 | -56.9655 | 2025-09-01 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| e24e5d68-8be7-3e95-b5d4-9218dc6d5546 | -10.6128 | -44.3284 | 2025-09-01 08:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1121f48a-4179-3bef-95fe-3e01cfbf4157 | -15.7289 | -48.9892 | 2025-09-01 08:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5c7014f6-e1b2-3df3-91ea-db0fc79f7463 | -11.0464 | -46.9618 | 2025-09-01 08:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 67d3f4c7-dbcb-3c03-aa89-13c40190e195 | -11.0381 | -45.1256 | 2025-09-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 44511c2b-4d60-39aa-9a02-08507541ab6e | -10.5937 | -44.331 | 2025-09-01 08:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 85571c1f-028d-3ebe-a164-3bd09e2620bb | -7.9539 | -46.4542 | 2025-09-01 08:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c7f31404-a43c-3d4f-9fac-82cc8f029dc6 | -7.076 | -44.3376 | 2025-09-01 08:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d900aca9-5cb3-356a-bc6e-989af0fed180 | -11.0377 | -45.1487 | 2025-09-01 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| e8f73f53-e5c9-3c73-bcfc-9e3e626d5d48 | -12.9197 | -56.9471 | 2025-09-01 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 834be371-7357-3dc4-81f5-b0ba8de09495 | -7.9351 | -46.4559 | 2025-09-01 08:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 852d561b-8d63-34e8-bc10-508528b8bbd9 | -7.9539 | -46.4542 | 2025-09-01 08:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 2c5bd151-55aa-3c54-89ea-af3547ef5efb | -15.5862 | -48.3435 | 2025-09-01 08:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d8129396-2688-304b-9dd1-3395648f5854 | -15.7289 | -48.9892 | 2025-09-01 08:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 890cfc0d-dd1c-3bae-a281-2683129c30c9 | -11.0568 | -45.146 | 2025-09-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 73bab033-e9a4-3ac6-a7cd-8aa7f3bc87be | -7.076 | -44.3376 | 2025-09-01 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 70efe641-f676-3e59-846c-bcdacbeb8ea2 | -12.9385 | -56.9655 | 2025-09-01 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 6d09497e-d4ee-3c9a-b4a8-22212056a5bc | -7.0948 | -44.3358 | 2025-09-01 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d5b64d92-e551-35c6-919d-866f0c961b40 | -11.8185 | -46.4087 | 2025-09-01 08:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| eecedfa8-8391-3217-bba4-c8f0306abdb3 | -11.0572 | -45.123 | 2025-09-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 9a1ef738-084e-3c5d-9986-0e53deabeaf6 | -12.9387 | -56.9454 | 2025-09-01 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 798d9563-4d34-3479-974a-3cb6606fc8fe | -12.9194 | -56.9672 | 2025-09-01 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 62adb330-ae0b-35b8-aa16-0291000e0237 | -10.2488 | -51.1128 | 2025-09-01 08:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 6b405362-67ac-3a5a-b6c0-7b94a164698e | -10.6131 | -44.3051 | 2025-09-01 08:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6e30c917-d18e-3dfd-aaf8-ff98f4116d05 | -12.9197 | -56.9471 | 2025-09-01 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 97faf025-378b-3b44-b251-6f55a5d6ce8a | -7.0946 | -44.3589 | 2025-09-01 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| eb12c844-4f10-3811-b8c3-ba085da37b99 | -11.0377 | -45.1487 | 2025-09-01 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| df18d4c3-046c-3100-a599-86e0eeb5a9ff | -7.0572 | -44.3393 | 2025-09-01 08:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| bd97fceb-82a6-334a-b1e3-ef276ec47a4a | -15.5867 | -48.321 | 2025-09-01 08:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9a8d4e8c-bd8a-301c-9256-9b0cbd536062 | -10.6128 | -44.3284 | 2025-09-01 08:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| e49a0cd6-5024-3a4c-8ab0-6b6a694b6aae | -15.7116 | -48.8809 | 2025-09-01 08:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9264d9fd-e103-39e3-8b58-65e7db72eb55 | -11.0648 | -47.0042 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 306.8 |
| 096725d4-1092-313e-955c-ba6ef5d86391 | -7.9539 | -46.4542 | 2025-09-01 08:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7972f5e8-de1a-347f-8fce-70991264b8f4 | -11.0572 | -45.123 | 2025-09-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| adba83bd-879f-3f67-98ad-ad9970f7f05f | -12.9385 | -56.9655 | 2025-09-01 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8aad8595-f2f0-321a-8fad-48f2d6d7f91f | -11.0457 | -47.0066 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 331.0 |
| f529334c-74b2-343a-9818-6a26ca1e36d0 | -7.0948 | -44.3358 | 2025-09-01 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e21f1b51-f17c-3293-95b9-4173837e7a8a | -11.0377 | -45.1487 | 2025-09-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 1c05f83d-8519-3fb4-b249-aff2185adc5a | -11.0461 | -46.9842 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 3f3fcee9-0b8d-3ca2-8473-dc0e71ad3ffd | -15.5862 | -48.3435 | 2025-09-01 08:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| baa18e30-26b4-314e-9a99-d6aae2c2644e | -11.0645 | -47.0266 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| b9d49e88-9a1f-3963-87ba-6ed591e8be2e | -11.0568 | -45.146 | 2025-09-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 20deafac-6400-38c0-9e5f-3b389916c918 | -15.7289 | -48.9892 | 2025-09-01 08:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8a46882d-2cab-3770-93e0-7447cbef8c79 | -7.076 | -44.3376 | 2025-09-01 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| c7220fe0-7d01-3136-a251-48437e950c6f | -10.6128 | -44.3284 | 2025-09-01 08:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 7cafce50-e125-34c4-9e5a-332b392d5454 | -15.7116 | -48.8809 | 2025-09-01 08:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 611677ec-deba-3be9-b7cf-15e91ec82206 | -12.9197 | -56.9471 | 2025-09-01 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| ed54d66a-2e92-3363-b61c-43fb7bb22f21 | -7.0572 | -44.3393 | 2025-09-01 08:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 078aae92-ece5-33c5-b47f-d1e847fd563e | -11.8185 | -46.4087 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b99d91fb-63b8-3fdf-a162-4e76c593bade | -11.0652 | -46.9818 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e450a112-c8c3-37da-a4ee-6a884d096d85 | -11.0454 | -47.029 | 2025-09-01 08:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 992f4aec-2c19-3d0c-a646-09ed5cb3ae4d | -12.9387 | -56.9454 | 2025-09-01 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 31686c02-d7e2-3aa4-add6-9ad5b6211674 | -12.9194 | -56.9672 | 2025-09-01 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 28a408db-4f14-34f3-a384-6d6103f64095 | -11.0381 | -45.1256 | 2025-09-01 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 3ddb536d-27c6-3a74-a3cf-7edc588f8c91 | -15.7289 | -48.9892 | 2025-09-01 08:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4e0b1eab-b2e4-3137-9037-e0a3f63357ba | -7.9539 | -46.4542 | 2025-09-01 08:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0ee90c30-56e6-3d7a-9baf-6787fd3ddaba | -12.5718 | -48.228 | 2025-09-01 08:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fddd6d51-13ea-30c5-a0fb-c49ba776be0b | -7.9536 | -46.4765 | 2025-09-01 08:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ac834690-f6c9-3423-a8de-bd606e0553c7 | -12.9194 | -56.9672 | 2025-09-01 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d33fddf1-b4b1-3b42-bc0e-b2474e98fdac | -15.5862 | -48.3435 | 2025-09-01 08:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 18754825-b98b-3c4c-b819-23d5733c1b9e | -7.9351 | -46.4559 | 2025-09-01 08:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e2e9bae6-22fb-3a7e-9668-1ed219df5f7b | -12.9385 | -56.9655 | 2025-09-01 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| db5a5bfe-62f3-32c0-bdce-1eb6ba25cd68 | -15.5867 | -48.321 | 2025-09-01 08:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| c717d318-53e9-3f5c-9823-28a15cf00c31 | -15.7116 | -48.8809 | 2025-09-01 08:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0f46a2d5-5889-35eb-8b7a-9ff9c27a7f13 | -12.9387 | -56.9454 | 2025-09-01 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 51107bed-c2ca-3749-8bdb-22ec7abbfe9e | -12.9197 | -56.9471 | 2025-09-01 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ad6ebc7c-0f6e-3a8d-b616-b59aba8c0385 | -15.5862 | -48.3435 | 2025-09-01 08:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 106.3 |
| ed8d9aaf-99b7-3b44-98fa-f00f145b14c3 | -12.5722 | -48.2059 | 2025-09-01 08:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 11a9ec0d-5864-367d-9e29-c8737e310963 | -15.5857 | -48.366 | 2025-09-01 08:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ffa4a770-b4e6-31fa-b09f-0d1cb29d0ac8 | -12.5718 | -48.228 | 2025-09-01 08:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| d17b45c9-cb76-3dfd-9558-e85bc6625493 | -15.7116 | -48.8809 | 2025-09-01 08:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 7470e269-d787-38e9-98e4-f67fe507029b | -12.9387 | -56.9454 | 2025-09-01 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e59dd7ee-15b6-3aa3-bb0c-a7b6bbc9e2b9 | -12.9385 | -56.9655 | 2025-09-01 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 2e0e62e1-9a98-38fb-97f1-0537eb5c7184 | -12.9194 | -56.9672 | 2025-09-01 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 14b54c56-8f6c-3853-9289-114ef9e90ebc | -12.9197 | -56.9471 | 2025-09-01 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 9050ab8a-b876-3374-b5fa-de15e2b19c9c | -15.5867 | -48.321 | 2025-09-01 08:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 64099685-7a00-37cd-9392-30738e5ae847 | -12.9194 | -56.9672 | 2025-09-01 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3e10b238-d201-38b0-860d-6b7d9e6637d0 | -12.9387 | -56.9454 | 2025-09-01 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c08b66e3-841e-31a7-9897-8a4d21bcf877 | -12.9197 | -56.9471 | 2025-09-01 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| b3cff158-b04e-33dd-938a-1f7a7cc0f50b | -12.9385 | -56.9655 | 2025-09-01 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 01c9b4f6-3d85-3d6c-826a-00d7644e8444 | -11.0568 | -45.146 | 2025-09-01 09:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 83676c88-0048-3926-b0ed-47df0aab055b | -7.9536 | -46.4765 | 2025-09-01 09:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 70a6efa2-dbde-3872-930b-7528dd775228 | -11.0568 | -45.146 | 2025-09-01 09:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 80768227-0cb1-3b4e-a140-2e2f28a19f2b | -7.9539 | -46.4542 | 2025-09-01 09:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| ad93a986-e6a0-319f-a7c3-d98896220697 | -12.5718 | -48.228 | 2025-09-01 09:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| ae4c40c9-ec4f-37b6-84d5-5565167c3de0 | -12.5718 | -48.228 | 2025-09-01 09:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 5a724b7a-32a8-3cb6-be38-8cd0bb3c4d7b | -11.0568 | -45.146 | 2025-09-01 09:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 5e0334b4-0723-3717-8f6e-87d48b214fe3 | -11.0377 | -45.1487 | 2025-09-01 09:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 345f60ee-e4c4-32c6-bc37-7c58f92e043a | -11.0377 | -45.1487 | 2025-09-01 09:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| ab17ca24-59d1-3505-b653-1ee7a6b1e57d | -11.0568 | -45.146 | 2025-09-01 09:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1f789e58-16ff-3dae-9b67-822633795f62 | -15.5862 | -48.3435 | 2025-09-01 09:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 9cb00d40-1082-3357-8c90-be120beaa2d0 | -15.5862 | -48.3435 | 2025-09-01 09:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 4301ca06-482d-3605-9688-b67a72289198 | -11.0568 | -45.146 | 2025-09-01 09:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| c0240109-26c3-3fb6-8a60-3c1440e0e6ca | -15.7116 | -48.8809 | 2025-09-01 09:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 254.3 |
| 0111b3af-f61c-3631-a1a7-9af5c0e053bf | -15.7112 | -48.9032 | 2025-09-01 09:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |


[Clique aqui para ver as próximas entradas](README100.md)
