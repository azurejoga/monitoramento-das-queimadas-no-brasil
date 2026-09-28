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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f1b9cdc-77a2-35a6-85ae-74b4133a3b5f | -11.66443 | -43.52684 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c772619b-c066-3eb9-a2b8-7e05df676d12 | -14.3847 | -41.42268 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7896a7e5-7c3c-30b0-952f-df23733f6cb5 | -12.63273 | -47.263 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e9ce2e3-81e9-3bfb-bbc1-a440c94daf87 | -12.37302 | -50.23058 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2a5551d9-0eef-30c0-92d5-30119b659de8 | -13.3468 | -51.32752 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9b1c398d-4da0-3a5b-a345-f112cf8935a1 | -12.37564 | -50.23963 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 565f0d0d-72a8-30a2-917f-a0ecff443638 | -14.53339 | -48.30204 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2eb52925-8972-3c66-8287-7ebcec093389 | -12.07808 | -46.48092 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cbddfbc3-de1e-3698-9322-5dc730c17d26 | -12.68882 | -45.01596 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 36a56039-06af-370b-824f-a5f5e27bbd04 | -15.18672 | -46.14742 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5b6188ee-beb2-3445-af09-7b7f69565e77 | -15.55892 | -47.9299 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01eb4485-8ef4-38a1-9321-04378a67b186 | -11.68301 | -39.81132 | 2026-09-28 16:24:00 | NOAA-20 | CAPELA DO ALTO ALEGRE | BAHIA | Brasil | 2906857 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c29dbead-5bae-334d-8413-937c77f74a43 | -15.20485 | -50.24327 | 2026-09-28 16:24:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9846da3-a1d3-3129-b852-b24581efa096 | -13.08748 | -47.44367 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c44149b-85d2-3a81-9cd4-4b9312ddd6e1 | -14.2492 | -39.94602 | 2026-09-28 16:24:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d2ac6c0e-02e4-3ffd-86c1-36ae5bc03fec | -15.87576 | -40.76381 | 2026-09-28 16:24:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3fb5dae2-2120-3cf2-9d10-52689c5faf05 | -11.36945 | -43.42162 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 98cff0fc-d9da-3747-bb0b-f8bbd027cf3e | -11.2201 | -44.78604 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3ee8bc5e-9f56-38be-9038-8e5e890bc46b | -15.11302 | -44.09022 | 2026-09-28 16:24:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 46ccf3f3-2e4f-3c05-a44d-e55faaab52b7 | -12.68481 | -46.97762 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74f5ca2d-6b7d-3f25-bac3-1126c27165c7 | -13.45296 | -48.59107 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9b689765-42a2-3283-b30d-668e6f87d0f3 | -15.66804 | -50.22097 | 2026-09-28 16:24:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c7bf0e5-696f-3245-95fa-5da26af6b55b | -12.74484 | -47.3274 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b4ca47d6-e76c-30bd-b553-f115c4146997 | -15.54121 | -40.70611 | 2026-09-28 16:24:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c49d217e-d682-3012-942a-6e0eace8c54b | -15.98662 | -48.4155 | 2026-09-28 16:24:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| df046405-5005-3784-b9e0-560ada28d173 | -12.87344 | -44.81541 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 60e18212-5069-3722-9e91-c8b382c45df9 | -13.44375 | -48.61739 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aabe57d4-09fa-3e55-bcf2-44ae2fe7a67c | -14.50895 | -40.85611 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 75daa4b8-c87f-3303-bbe6-0afebc250cbf | -13.6916 | -48.81919 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| af1054f2-5894-383e-bc19-05632bc4126a | -15.22077 | -46.18535 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5f6f3a2b-7d99-3205-97ce-7819a5d8ee85 | -16.21448 | -48.82817 | 2026-09-28 16:24:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aec0e983-ea28-3d36-8684-df45a6e04bb0 | -13.3036 | -39.39894 | 2026-09-28 16:24:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ffad3616-a8bf-3ea4-9356-fa5b406d50fa | -16.86232 | -50.15438 | 2026-09-28 16:24:00 | NOAA-20 | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 471ecdb6-8406-35cc-a4ca-71efe51908bc | -11.05264 | -42.9874 | 2026-09-28 16:24:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 28706acf-1cec-3639-96a6-400cd2e00d8c | -11.70891 | -44.54936 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 74e02ba6-6a39-3142-80cb-37fb3e426eba | -14.51244 | -48.32574 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1a659931-4a8c-39db-a87c-b10cd998823d | -11.38524 | -43.43446 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 7a74a2aa-dbeb-345f-b595-9010b5bae7f8 | -16.43743 | -47.49174 | 2026-09-28 16:24:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24a779f4-2b0d-32ce-83d4-7ca4e6fc3dac | -13.94526 | -49.07156 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7ced7d5c-e80b-3113-a898-b306d5ed81c2 | -12.70689 | -47.33677 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 78025a93-2322-3906-9a19-dc781ed18642 | -12.7387 | -47.28182 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 898e2b9d-494b-3248-9cfd-8c32582c0194 | -13.10727 | -47.41198 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d079072e-b2da-362b-8b0c-695dce6660da | -14.53178 | -41.16177 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 40cb9253-8c99-36a9-9e1d-33232390a3c6 | -12.67799 | -47.34898 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 83c9c035-753b-3ca2-a544-0515206bee4a | -15.18119 | -46.1366 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0b60a5b0-7df4-35b3-badd-2eb21bee1269 | -15.50651 | -49.90149 | 2026-09-28 16:24:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 913e00f6-be98-3746-b192-4185a2a7a9fb | -14.51929 | -48.30363 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c30c1eb-8da7-3b7c-8c6d-8f31a8423101 | -12.70098 | -47.32496 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 788a7241-7038-34de-9e69-5cf0118258a4 | -13.47347 | -48.58603 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e19b26cc-31b4-3a80-9ab6-f57afc0cdb5e | -15.03387 | -49.59441 | 2026-09-28 16:24:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0d55055a-ede1-30ca-ad32-8e0bf783b4b7 | -12.68871 | -47.36434 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 094a0e04-9802-3ab5-87e3-4d2a2b747701 | -15.34611 | -42.16689 | 2026-09-28 16:24:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 58207217-6358-358a-b250-5169b6a79897 | -12.13752 | -50.35057 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29b40204-18e7-318b-8cd0-12dc5d8a9d55 | -11.64124 | -43.48801 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b231e3e3-df2f-311a-87f4-30d1ef259910 | -14.41334 | -40.69698 | 2026-09-28 16:24:00 | NOAA-20 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| e8b7c2f5-bc41-3b55-8dcb-90739ffb6852 | -14.08794 | -46.3209 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ee11f8cf-72c7-3da6-929e-102a65fde87e | -11.39097 | -43.42601 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| aa2cb365-8874-3700-af74-95936789b00b | -11.38158 | -43.38561 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ec08c6-e988-39a9-aa0a-2fb2c09d11d4 | -14.38342 | -52.10032 | 2026-09-28 16:24:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e2604374-2d71-333a-a583-ed80551cf7a7 | -13.97221 | -53.96913 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92bc58de-7c9f-30d6-ab0c-fb8997281e57 | -11.51712 | -47.38933 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 0a04a1f5-7c37-37d3-a2e4-3ae6f15d5087 | -11.91108 | -47.02019 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6fdd7a2b-14c9-3541-bd8e-684b979e0d5f | -11.20542 | -40.5872 | 2026-09-28 16:24:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c981f752-1bc3-3ac7-9d30-e91c2cd25537 | -12.31778 | -40.23291 | 2026-09-28 16:24:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a825d380-678f-3f0e-8940-9ea7ee0eeaf0 | -11.17454 | -44.80105 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 96b89de7-5573-3c32-9287-562e2d7d6b13 | -12.07018 | -48.54349 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 529.2 |
| e04876ef-6113-38cc-8a69-fe68e47a105a | -16.1966 | -41.20433 | 2026-09-28 16:24:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6e04c6b9-afc8-33b6-97fb-a8de3426205c | -14.58392 | -41.23722 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ac3fb63f-0eec-312c-b232-ecea64245fa0 | -16.2878 | -40.19839 | 2026-09-28 16:24:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| c4ff2007-d317-3c8b-b910-5f6f4196586d | -14.09485 | -41.39004 | 2026-09-28 16:24:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4c804d95-d8af-34e0-9d97-746eeca514b2 | -11.5652 | -47.39502 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5f4b075f-4000-3171-9afb-6cfb49e641a8 | -14.32382 | -44.81871 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 95aee22e-454d-35cd-8313-9cca65293620 | -12.07357 | -48.53329 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 6c989b06-432f-3c2f-a1af-3fa27ba3f080 | -12.68442 | -47.36489 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ad1c099f-bdf7-3e35-8d48-36c9096f5ea7 | -16.57303 | -39.45617 | 2026-09-28 16:24:00 | NOAA-20 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 01ad87d3-99cb-3064-b701-fbc322670bca | -15.7407 | -41.878 | 2026-09-28 16:24:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 09191074-5846-324f-bf05-87d28690a764 | -12.75433 | -47.30099 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1eecbfea-91e4-34d1-996c-b1b654e7681b | -15.77096 | -39.02067 | 2026-09-28 16:24:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c8a9ea5f-9890-3d09-9cf4-782d14deb763 | -12.16605 | -50.40903 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8069bd02-46cd-3f7d-8fa0-ad5d15bf89b5 | -17.57398 | -46.90885 | 2026-09-28 16:24:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c555afd9-ecd1-3652-a080-9b453daeb5a9 | -13.92805 | -47.85458 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 70d0337b-0936-3166-a813-689ac605b2c1 | -14.73328 | -41.0589 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 564b9ef6-a6fc-3a89-b65e-78b91fb5c942 | -16.63314 | -48.47521 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d632dea0-a550-387b-bf6f-89280836d49e | -11.63837 | -43.49229 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| e7aac06d-0477-337e-a8eb-f659ae516dd4 | -11.17873 | -44.80466 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| fa9055a6-2931-3a17-90f3-85ec5b7823fd | -15.44527 | -41.44078 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 90724f73-f8f3-391b-a565-0e9aa9b391bc | -13.33408 | -46.81152 | 2026-09-28 16:24:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 19af6dfe-cf60-38e5-bb03-783150745c2b | -14.61338 | -41.02831 | 2026-09-28 16:24:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 60d0e94b-8bc0-3694-b1f0-e39bc967e7b2 | -14.20148 | -44.93757 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8de36c13-ed6a-3611-93af-02807f7512ad | -14.53218 | -41.34394 | 2026-09-28 16:24:00 | NOAA-20 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 8fef2cb5-f8ea-3485-bb97-a0b526ba5999 | -11.91057 | -47.01638 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9eeb1b13-7563-3b92-bf54-d9a15777fe79 | -11.19672 | -44.8021 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 9a7dcf34-d4c0-31a7-a15c-51a6493d262f | -12.17292 | -50.42131 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7e90c3e-d6f1-3848-9552-d84e2f373325 | -11.37586 | -43.39407 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 62ee43f4-5ce2-3541-af6b-bf7dd3938384 | -12.17826 | -40.73013 | 2026-09-28 16:24:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| a4f38051-678c-33fa-bf57-c0bffc2976ef | -12.81028 | -54.00846 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 6ddb416f-6bc0-3a21-ac9f-3017cb10d628 | -11.90846 | -49.99061 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5526ffda-151d-365d-a913-aac1b89f8ff9 | -13.26293 | -47.44458 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 429693db-ae2f-32e3-be12-178b42c65a3a | -13.94036 | -49.07217 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c61e2507-e299-3706-bce4-a31daee9a2cc | -12.44801 | -48.22185 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README101.md)
