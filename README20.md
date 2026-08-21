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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81881555-a7a3-3adf-9f19-306184eb5ed9 | -9.4069 | -60.4362 | 2026-08-21 03:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 264fa978-2083-3b49-9eb7-7104d3d92e17 | -6.2341 | -55.6109 | 2026-08-21 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 637c304b-ff53-305b-afba-bf990173fd7d | -13.3737 | -54.3572 | 2026-08-21 03:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0311daa2-e6f5-372a-900b-2c2fd6a77867 | -20.99652 | -43.3299 | 2026-08-21 03:10:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0fe8bb9a-92ad-3f4f-8b15-3adea09114f3 | -21.88518 | -41.47662 | 2026-08-21 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7114cd47-6c84-3d5e-b101-033246c545b6 | -22.38087 | -43.02219 | 2026-08-21 03:10:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 97a88d57-723c-3f2d-9c79-4cdadfe95a97 | -20.42119 | -41.58963 | 2026-08-21 03:10:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5beb63e2-d746-3328-b5a5-89832e294de3 | -21.57653 | -43.48243 | 2026-08-21 03:10:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 478a3169-5580-3c25-98da-7fccbe5cf9c3 | -21.32632 | -43.81393 | 2026-08-21 03:10:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cd651507-d4c0-3391-84e8-50b4c8231158 | -19.85715 | -43.87682 | 2026-08-21 03:10:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4f54b9b5-3c91-3858-8473-b272acf1fb4b | -19.85335 | -43.8751 | 2026-08-21 03:10:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 54c24e5f-bc16-3ae9-8e62-bfafc9a1645d | -21.36776 | -44.13121 | 2026-08-21 03:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 47aba3a1-fde7-3022-803c-a83186d2c5f5 | -21.32798 | -43.8073 | 2026-08-21 03:10:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 68034af8-9c19-3615-93d1-1d5a53140a96 | -21.36348 | -44.12951 | 2026-08-21 03:10:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 862614a0-e3be-39e1-a2b4-999a6e2b815f | -20.99819 | -43.32314 | 2026-08-21 03:10:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ad6e088-1118-3ff0-8120-609aad2d6a42 | -22.38203 | -43.01747 | 2026-08-21 03:10:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e88e4bae-8bc2-327c-95e7-10f47b9094fd | -21.57536 | -43.48064 | 2026-08-21 03:10:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 20f11f4e-a3c5-3411-ab5b-9daa049ff32e | -20.63835 | -41.20796 | 2026-08-21 03:10:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e624ed93-25dd-3551-9192-e1af05771ad3 | -19.84988 | -43.87584 | 2026-08-21 03:10:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 051b5b95-5fa7-3682-bb97-ced5967d9691 | -7.34 | -45.85 | 2026-08-21 03:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9f8a5d-c4f2-3dfb-8ad6-650313823fc9 | -7.37 | -45.8 | 2026-08-21 03:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2c58a42-e71c-3bb4-8eea-7890512bdeca | -7.34 | -45.8 | 2026-08-21 03:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2c1670ec-5882-3258-8ec5-a3a3f40f6533 | -6.1177 | -59.9069 | 2026-08-21 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 270c012d-50ec-3eb6-8397-e8d56e8954ff | -6.8388 | -59.3993 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9b2ae4e9-30ba-3115-8ba6-5bc22b6144d6 | -3.5406 | -48.1889 | 2026-08-21 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| caeacc8d-4ddc-3346-8e4e-4edeec26c802 | -11.1747 | -54.0216 | 2026-08-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 83da64ad-b998-3e29-8ded-d3646e85ae96 | -12.5101 | -54.7755 | 2026-08-21 03:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6ba31998-9ca8-3e04-be75-a88e5f2ac609 | -12.4914 | -54.7569 | 2026-08-21 03:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| cbf97ba9-81d0-3bed-82ba-929fa6474b4c | -12.5104 | -54.755 | 2026-08-21 03:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 3504f668-fc88-3e83-a437-00d2eb731e9e | -10.8358 | -50.9903 | 2026-08-21 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 11d0efc0-90fa-32d3-afa8-9a969af420d5 | -6.2341 | -55.6109 | 2026-08-21 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| e4e945dd-0c1a-3c4d-903e-911d2c8a390c | -6.8019 | -59.4008 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 1f44abca-8de4-3355-9e0c-1ef530e4e462 | -5.598 | -43.9978 | 2026-08-21 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 996ce5d5-5078-3813-88f4-746a7fb4a1d6 | -10.8355 | -51.0116 | 2026-08-21 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 103b2da9-444a-3fd0-93f5-d880c3165e39 | -11.1558 | -54.0233 | 2026-08-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b4790f32-7ed3-3c16-afab-e0554b0b23c9 | -10.8169 | -50.9923 | 2026-08-21 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8ad9f582-a483-3e07-8c07-b42562ca07f7 | -11.175 | -54.001 | 2026-08-21 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 92f16174-dfc7-3577-a834-da70280092b8 | -6.857 | -59.4371 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 51120a62-b166-3337-8c8a-c5ccd039840c | -6.8755 | -59.4364 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| e82e690e-285b-3c91-8d78-23289b9486f7 | -6.2155 | -55.6316 | 2026-08-21 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5bfd527e-4595-3b36-9ce9-02a38298d162 | -6.6938 | -58.942 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0c26f877-b6e9-34b7-b2d3-61b1f9637fc3 | -6.8203 | -59.4001 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| b13800a4-70b3-3a7b-8d02-407ee80539d7 | -6.8204 | -59.3808 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5e1e3d84-a546-39d2-be7f-de9fba223c18 | -6.2156 | -55.6118 | 2026-08-21 03:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ed7a8d05-7d54-3fbf-8030-bde8faa1c1b1 | -3.5407 | -48.1673 | 2026-08-21 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c7ac8d8f-ad30-36ec-9c0d-dc2eed07a091 | -6.8756 | -59.4171 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 8d1bcb14-5b8f-32ed-b16d-23892f50c6ff | -8.3903 | -62.6963 | 2026-08-21 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| cad39a31-8c92-3cef-b4d0-7e38993fb69b | -6.8939 | -59.4356 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d3c20a4c-5db5-3a49-a278-0bab8140e998 | -6.8202 | -59.4194 | 2026-08-21 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 7cf2eacb-419f-3a91-91b8-770a0939740d | -8.3902 | -62.7152 | 2026-08-21 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 28174598-6130-33a2-b9b5-9448dac4bd1c | -10.8166 | -51.0135 | 2026-08-21 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d456b5ab-3a5d-3c80-8fd0-76d0b0c12c1a | -13.3923 | -54.3965 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2c452682-e4c8-324e-9c34-4b345d67b572 | -7.3791 | -45.8119 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 2091f460-03be-3d26-853f-c1a0bdd6f8f7 | -6.6938 | -58.942 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e2abf5f5-d503-3f39-b0da-3c6ac2884dea | -9.4257 | -60.416 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 5e7116c1-066c-3bbb-82f4-79ed81b80312 | -3.5407 | -48.1673 | 2026-08-21 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 11d82e97-dc60-33c7-bb82-76d8eb2e21f3 | -12.5104 | -54.755 | 2026-08-21 03:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| eb50771d-1ad2-39f5-834a-4db728e16663 | -9.4259 | -60.3967 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a557550e-45eb-3242-a2ef-833466d5cf5a | -5.5978 | -44.0209 | 2026-08-21 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 97231e9b-17d0-3f43-aacc-1f8af2558220 | -10.8355 | -51.0116 | 2026-08-21 03:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 342a15ca-85e7-36cd-ad71-c1d47f495ff4 | -13.3926 | -54.3758 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 372.5 |
| 65e795ce-54f9-3641-8ad3-7c3a74876549 | -7.36 | -45.8361 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1743d6b1-0064-316f-bae8-f7962b1b34ea | -6.2156 | -55.6118 | 2026-08-21 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 3ec41674-1b11-3e3c-b1b1-1ca26df6974f | -3.5406 | -48.1889 | 2026-08-21 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 7470822f-728d-3417-8b9f-ee9fb8e5363a | -9.4071 | -60.417 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 252.3 |
| 88d554ba-e4c7-3f30-b6d1-48314d7b1737 | -6.8388 | -59.3993 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8c0a00df-6e59-358a-a1fa-4977ce7c6efc | -12.4914 | -54.7569 | 2026-08-21 03:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c1c893e9-5683-3219-9420-ec694cdfb800 | -6.8939 | -59.4356 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c4bb3567-a750-3621-8495-8dcfd2d445a9 | -13.4117 | -54.3737 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f06db7be-057b-30eb-9d42-45c0895ad4bb | -8.3903 | -62.6963 | 2026-08-21 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 954f208e-13a4-36c8-be10-2b5cf10661d7 | -9.4069 | -60.4362 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| e866710c-fb29-3f66-aac3-7617dfe9cbef | -7.3605 | -45.791 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 3d00203a-7464-3f9d-bbff-0b7a136239e2 | -6.857 | -59.4371 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e7e093b3-bd48-3e1a-a761-c1b1edaddb13 | -4.0481 | -50.2984 | 2026-08-21 03:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 21904b4a-50b6-3905-85a9-3bdf6f4d5e8e | -13.3929 | -54.3551 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 4a86491e-7974-38ed-911d-627ff2404433 | -6.8755 | -59.4364 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 23292af3-5e24-30ab-a286-4e0737cfb4e4 | -9.4072 | -60.3977 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b2308cd7-a3e4-37b4-ab41-9944fdbf46c0 | -7.3603 | -45.8136 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 345.5 |
| be240671-611e-30d9-b2be-8de1519f10be | -6.1177 | -59.9069 | 2026-08-21 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0176167b-2947-3e38-a599-a15dd11c4deb | -6.8756 | -59.4171 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 3daa236f-a194-3f87-bc47-7c2541a05fd6 | -6.8203 | -59.4001 | 2026-08-21 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 28934901-6180-3233-b067-332c2c2bd8e3 | -9.3885 | -60.4179 | 2026-08-21 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 4651b475-e09b-3527-812d-5fe6b6376b49 | -11.1558 | -54.0233 | 2026-08-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1a3f4261-3cae-37ce-8b44-b10082067766 | -13.3737 | -54.3572 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 4523166a-43e7-30cb-8a36-b667acb061c1 | -6.2341 | -55.6109 | 2026-08-21 03:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 9ea4337b-1967-3cc4-b92d-fd108ef82f76 | -7.3415 | -45.8152 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0c316463-433a-39df-bea8-5d4bdb224b3c | -11.1747 | -54.0216 | 2026-08-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 997ef2c4-9b7c-37ea-98e7-e2c6cd151f96 | -13.3734 | -54.3779 | 2026-08-21 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 433.0 |
| 0dd6e9be-9cde-36ed-8eb6-07a1c0afbbfc | -7.3793 | -45.7894 | 2026-08-21 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e8416dfa-f274-3a57-8e3e-4f429bf80ca3 | -11.175 | -54.001 | 2026-08-21 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 67a5cf05-fb7a-38b5-a4ab-23c9973e30d7 | -5.598 | -43.9978 | 2026-08-21 03:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| f742c0cb-6389-3540-a42f-a79fad7b9c33 | -7.3605 | -45.791 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| f1cd668e-7bbc-3b23-bb1b-684b43c9fa17 | -7.36 | -45.8361 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d4ff4ec6-c88c-3745-92b2-44564831f2e4 | -12.5104 | -54.755 | 2026-08-21 03:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6107f7a7-7265-3376-949a-f2cd3319572d | -12.4914 | -54.7569 | 2026-08-21 03:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1c36029a-d6d4-30d3-8d55-436fb232bda3 | -3.5406 | -48.1889 | 2026-08-21 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f3f97aaa-9ce9-38bc-a4d2-44c29230d3ad | -6.8755 | -59.4364 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 8fc0f19e-28ca-3a2b-a83d-024352959e6b | -6.857 | -59.4371 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 448845bf-d021-355b-991d-fe8af0aae2e7 | -7.3793 | -45.7894 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 819491ee-f458-366e-9a5b-52763f7d5082 | -11.1747 | -54.0216 | 2026-08-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |


[Clique aqui para ver as próximas entradas](README21.md)
