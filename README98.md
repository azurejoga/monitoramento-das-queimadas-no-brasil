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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56dddd30-d174-3dd1-94a6-013c02885558 | -20.8042 | -44.5659 | 2025-08-27 14:20:00 | GOES-19 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.7 |
| 62d5002a-4d22-35bf-82c5-27594ede4e84 | -12.7259 | -48.1846 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5dd03829-efc7-3e0c-9b8f-4625e576dd1e | -9.0771 | -66.0695 | 2025-08-27 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 27ca190d-9c5b-3295-912b-cb4180fad3d4 | -6.8875 | -44.4004 | 2025-08-27 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3b855bf3-e2f2-38fe-8d78-e78ecd74075b | -6.8249 | -45.0003 | 2025-08-27 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e31b49a7-5f50-3b67-bff9-ac66427a1300 | -12.804 | -48.1072 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 576ed398-ba31-3a79-af64-6656f84c3093 | -11.7966 | -51.4169 | 2025-08-27 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 08cfe6ff-732c-3c8a-81c0-e7c7f3e8dd82 | -15.6362 | -52.7393 | 2025-08-27 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d8dc012d-8fd8-3142-9a87-d0c9bd991edf | -9.8286 | -64.2824 | 2025-08-27 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6607c45f-edf1-3578-a814-c85153dd056a | -7.6411 | -42.6955 | 2025-08-27 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 148.3 |
| 9b159d50-cfd6-3451-a671-c6ca00c6a277 | -7.6414 | -42.6718 | 2025-08-27 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 148.1 |
| 6d18c5f9-9625-3d71-889e-e584db83e613 | -13.4401 | -46.9834 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 3571b710-b2bf-3448-925a-a920c5173c37 | -9.1715 | -59.5599 | 2025-08-27 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 3bbbf8f8-11ac-3a3a-92dc-cd09118fb888 | -12.8036 | -48.1294 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 66f2e28b-a96c-348b-a8ca-b5ca12100678 | -9.2092 | -59.4997 | 2025-08-27 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 4d9f8837-15ad-3ab8-859f-6d8192e342be | -20.8042 | -44.5659 | 2025-08-27 14:30:00 | GOES-19 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 104.8 |
| d9b4d505-e478-34a2-85ff-47119e136eaa | -12.784 | -48.1543 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 6e88f760-426e-3f0c-bcde-cd0e594af02d | -15.6171 | -52.7207 | 2025-08-27 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a080da2f-cf2d-39e2-9eb2-9be8f4641da4 | -11.3146 | -43.5008 | 2025-08-27 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 382.5 |
| f6a06019-49a8-3b7f-9192-960ebdd0e52b | -6.4353 | -44.5993 | 2025-08-27 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 237c0703-251e-3dbf-b9b5-bb2df914c25e | -11.1587 | -44.7627 | 2025-08-27 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 275921aa-22db-347f-a712-f98c9c39eff3 | -9.4064 | -60.5133 | 2025-08-27 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| a2523a8d-9882-3bd6-9828-5332cc16ce74 | -13.0674 | -46.3153 | 2025-08-27 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 49aa5748-d0c7-3495-a5f7-b0b8a1288d77 | -7.4414 | -42.0501 | 2025-08-27 14:30:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 06f62d5b-a56f-3f89-bf1e-e9c96b40e7bd | -15.6168 | -52.742 | 2025-08-27 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 24a0d30c-cb1e-305b-8763-545980d1c206 | -7.3383 | -46.1073 | 2025-08-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 3be3d697-1b82-39c5-9726-b2137b19da44 | -8.9046 | -45.7067 | 2025-08-27 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 3b139878-5abb-38ca-9eb2-c6861be7ce1e | -13.6097 | -48.2126 | 2025-08-27 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 14d2a53f-e5b9-347c-89f4-d5e5b2e523bf | -8.271 | -45.1149 | 2025-08-27 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a366c562-e7af-3dd7-910e-3c71fc42b120 | -8.8855 | -47.1861 | 2025-08-27 14:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| b9fbe44f-dab5-31a7-b5e4-9263140aac72 | -12.7643 | -48.1792 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 99477c11-449d-3c26-8a2e-c8f5b70582b9 | -12.7639 | -48.2014 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 40b69dc3-9207-3368-906d-5e64c482e57b | -9.0816 | -49.6068 | 2025-08-27 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e6b3ef91-afb4-34fc-8a2a-1b3aea8b9e75 | -9.0819 | -49.5853 | 2025-08-27 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 66cca04f-d3a8-36ef-864e-caf5ae76d3b1 | -9.663 | -48.294 | 2025-08-27 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 524727f6-e63b-3bab-84ad-eff4b5ddea0f | -9.0586 | -66.07 | 2025-08-27 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3e570daf-3595-363a-8e0e-66e0f73075f4 | -11.1583 | -44.7859 | 2025-08-27 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 6647224d-f3cb-38ef-b7e8-67d870477fd2 | -13.4032 | -46.8987 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 7f7cb5f9-f086-3270-b343-f81c5879b177 | -8.9567 | -64.1272 | 2025-08-27 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 02e73a82-700c-3943-8502-84886cb6bd26 | -12.7263 | -48.1624 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e36e4adf-b399-3035-beef-719e44e5e8f4 | -13.5193 | -46.8805 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a4794bee-46d3-39b5-b939-48e549e57fef | -13.4036 | -46.876 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 152.1 |
| be8f844c-434f-3a9f-954f-7edc6959094e | -8.9112 | -46.65 | 2025-08-27 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e15e8c16-61d0-3745-b914-9308c717dc0f | -9.4062 | -60.5326 | 2025-08-27 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| b987cb50-c113-3fcf-9d7d-b82088138c42 | -6.6759 | -58.846 | 2025-08-27 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7e98e863-4093-37a7-8710-d9473016462c | -13.5382 | -46.9002 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 36e52bb5-7139-37fb-98c5-6f3a0a19f62d | -6.1785 | -44.0226 | 2025-08-27 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c173b4b6-1e0d-3505-95d9-7f8c51011f8a | -12.7067 | -48.1873 | 2025-08-27 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 98b0d1f4-2b6a-3c40-ac09-c929caa905a2 | -13.067 | -46.3382 | 2025-08-27 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ef0e9bed-40a1-326e-8016-36bca930d735 | -17.8471 | -47.7428 | 2025-08-27 14:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 8ce0461c-8f79-379e-a99a-04517fb2a184 | -9.0821 | -49.5638 | 2025-08-27 14:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| daf1aa85-fa89-356f-b798-4fceab46a9d9 | -9.4065 | -60.4941 | 2025-08-27 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7003e603-8057-3259-8122-bfe5a079ed94 | -10.6628 | -47.1881 | 2025-08-27 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 112ea611-bf8a-30d2-a3ed-bb2402382410 | -9.9352 | -46.38 | 2025-08-27 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1567488e-6b77-37c6-8e1a-239089712b42 | -6.4357 | -44.5535 | 2025-08-27 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cdf8bc4f-9c00-3d61-a823-47556d85a117 | -11.3342 | -43.4742 | 2025-08-27 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 863dd1ec-8631-338e-8ad9-52fc6f479ae2 | -9.6574 | -64.9845 | 2025-08-27 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 64aa36f3-1345-3dc5-bbe2-3cfc12503f1a | -6.4355 | -44.5764 | 2025-08-27 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 199.4 |
| c6742434-c005-3592-91a0-e8883f36ea70 | -11.3338 | -43.4979 | 2025-08-27 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 372.5 |
| 9854921d-c1fb-3e4e-8db0-7c713b9ed813 | -12.9072 | -44.6346 | 2025-08-27 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5bea893b-1528-3094-bd04-2eadeab3fac7 | -13.5378 | -46.9229 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5b343ec0-cedb-3644-9457-ba9678623cf7 | -6.1783 | -44.0457 | 2025-08-27 14:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| ffac9585-c313-3dea-b611-290ea3c5e7ca | -10.2742 | -64.5096 | 2025-08-27 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 220.7 |
| af07610d-951b-3d9e-a40b-25aed63de663 | -9.1441 | -60.7765 | 2025-08-27 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6f0b43a6-247b-378e-bf04-efd1f5e2a4db | -10.2743 | -64.4907 | 2025-08-27 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 989e3501-8b9c-3252-9b00-3b7f46bc2ac2 | -13.3843 | -46.879 | 2025-08-27 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 7bee8978-935f-3823-8dd8-28579933668b | -9.418 | -48.2756 | 2025-08-27 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 8a4fb36e-2b42-360d-9ce8-78b1da87b0cc | -10.2557 | -64.4915 | 2025-08-27 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| aac45851-a08e-30c3-b4ca-d822373ec055 | -6.8228 | -58.9753 | 2025-08-27 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6e74d24e-5432-3c35-b771-2a5770cf7384 | -11.1587 | -44.7627 | 2025-08-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 291.7 |
| b55bc7de-a7c5-32a3-bff2-bbf3abc4cbd5 | -9.4062 | -60.5326 | 2025-08-27 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| b94463d5-597d-3bdd-9289-9d2047fc6002 | -8.9567 | -64.1272 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 77d5e7fb-bcfc-3155-9600-14caaeddb532 | -9.418 | -48.2756 | 2025-08-27 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 4276cf32-2644-3d81-ba8f-8b595eb54892 | -8.352 | -62.9436 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e30418d2-1101-3e16-b3de-109baca5a0c2 | -9.8102 | -64.2454 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 3c4d3ffd-8abd-31be-8d13-2d84225d29fd | -9.2092 | -59.4997 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 862adc79-2afb-3c6e-bce2-51ef409b2a28 | -10.2742 | -64.5096 | 2025-08-27 14:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 211.4 |
| 27cfcfa2-aa03-3f65-946b-908bbb29bbba | -9.4064 | -60.5133 | 2025-08-27 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 8c5b4203-09f1-332f-8e96-6d82262a46dd | -9.0821 | -49.5638 | 2025-08-27 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3ab77690-fc90-3bc9-9a49-685f4da00975 | -6.1785 | -44.0226 | 2025-08-27 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9104a133-1dac-39b7-83c2-ba0f2b875381 | -13.5382 | -46.9002 | 2025-08-27 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5a21385c-7bb0-3386-a5a9-408ad0c82227 | -7.8983 | -44.7871 | 2025-08-27 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 760ddc6c-2447-336c-bb18-1cabc160437f | -9.6388 | -64.9852 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| a5f7017e-2440-3a56-a3f7-3d326d60f69f | -15.6171 | -52.7207 | 2025-08-27 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 85b92f51-f4c1-30eb-82fa-875c3c05456d | -7.4634 | -59.9123 | 2025-08-27 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| a5073046-c055-37f7-9af6-fd113068d552 | -9.2093 | -59.4803 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 875bfeb1-9d75-3d29-a4c8-5365119d4f94 | -14.3693 | -52.1026 | 2025-08-27 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| bc10e5d8-a75f-3366-8b4e-c27fc319524f | -9.1906 | -59.5007 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 8534bf3a-6799-3ae9-aae0-932a04b97854 | -9.8286 | -64.2824 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d0f1ea35-b962-3e06-920e-fa099f90d7a9 | -9.6573 | -65.0033 | 2025-08-27 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e0a18659-41c4-3b42-b572-d32e96e4bc8d | -8.8842 | -60.7507 | 2025-08-27 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 179.7 |
| db5ea7dc-1c20-3eb4-a701-0f1ca3f89bfe | -7.6411 | -42.6955 | 2025-08-27 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 46cdc09c-a07b-37a2-9b47-90254dbbf058 | -9.4065 | -60.4941 | 2025-08-27 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 93edd7fc-b88f-39a6-b3c4-9f62f055f1f8 | -6.1783 | -44.0457 | 2025-08-27 14:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 6c7ffc78-f977-3be2-b281-09aa87c97273 | -6.4357 | -44.5535 | 2025-08-27 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f686e341-d511-3e8c-ba49-a7229761bdb1 | -11.1579 | -44.8091 | 2025-08-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| cafd6ae6-7360-3990-a57e-817441c2d783 | -9.4183 | -48.2537 | 2025-08-27 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 094acebb-e357-319b-a975-d4c29f15a62b | -9.1004 | -49.605 | 2025-08-27 14:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 234a3c2e-85ac-31ab-bb3f-5a80a45b4a5f | -11.1396 | -44.7654 | 2025-08-27 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 09f317a4-0b09-38ac-957e-e42ac9b4c22a | -10.786 | -60.7848 | 2025-08-27 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |


[Clique aqui para ver as próximas entradas](README99.md)
