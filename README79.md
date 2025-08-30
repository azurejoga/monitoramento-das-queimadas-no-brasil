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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3952a324-c4e8-3d8a-b61c-ca8c78535ca4 | -11.89061 | -46.71466 | 2025-08-30 05:57:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b380e28f-59e6-3116-9089-928c03262c24 | -13.35258 | -46.8749 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9351a858-d47d-386c-82c0-9e2e660ddb96 | -13.36333 | -46.99257 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a018356a-6d4a-35f6-966d-5ee5bbb8ed1d | -11.15384 | -47.13853 | 2025-08-30 05:57:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26eeb608-f6e4-355f-ae83-03d331310c84 | -11.82273 | -46.47679 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb5ccf3c-0e4b-3b81-9047-1010468f9252 | -13.67889 | -46.91265 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c1ccc4fd-14ef-350c-861f-be9a253f4ec1 | -10.02065 | -48.05405 | 2025-08-30 05:57:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7c411c16-ab2e-3da9-ae78-1d18efe068d4 | -14.00826 | -44.57043 | 2025-08-30 05:57:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9d91182f-1d44-3f9b-9073-9578a6b70946 | -13.37508 | -46.97507 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1e9a9ba2-5e33-35f3-941d-eea65fbe82a5 | -13.55464 | -46.94576 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ebd9f185-995e-3074-9639-f84424e9006c | -11.84543 | -46.38298 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1d50e5c2-1114-352b-8938-ed1868716023 | -13.40628 | -46.95079 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ee720c94-1cca-3b58-8455-1f3134e1db7c | -12.84749 | -48.17 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f0665cf6-1e52-36a4-8359-626011f02762 | -14.45647 | -52.01969 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 39a2b48c-3975-367f-a87b-2b8c6473dfb8 | -11.86233 | -46.39478 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 9ee63128-27eb-376d-ba50-a44303d121ed | -13.37646 | -46.96561 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f4246ff-42af-334d-a747-eea23793020f | -10.02521 | -46.0261 | 2025-08-30 05:57:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81b9564a-3f20-31af-b8ed-41b69354560c | -11.83318 | -46.46855 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 82798fc9-4c5d-34a9-8f6e-0e27e7a94db7 | -12.40466 | -46.47146 | 2025-08-30 05:57:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ed703edb-ce4b-382e-927b-1b6bad718a44 | -13.42563 | -46.94068 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71682212-6ec8-3156-bcf8-3107c83175a3 | -11.32522 | -43.62525 | 2025-08-30 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7784dd99-8baf-39e7-b5c8-cbd0e935edf9 | -11.83138 | -46.86195 | 2025-08-30 05:57:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9bc1e08f-e399-3568-8734-c2a9f63061b1 | -13.39039 | -46.99663 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 34f66fa1-6f32-36fe-a81f-51efd3c2bf25 | -9.70182 | -49.46346 | 2025-08-30 05:57:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1e561464-4e19-3180-b7ed-9cbd503a1d3a | -11.93209 | -46.68233 | 2025-08-30 05:57:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 371b478c-3e6f-33e1-875d-90a61335976e | -11.32886 | -43.59798 | 2025-08-30 05:57:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0dee97f9-4322-35c8-b7f0-03f25ba28058 | -10.66638 | -48.72637 | 2025-08-30 05:57:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| e825eb0f-911e-31e8-8d0b-207a432c0fce | -13.37783 | -46.9561 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| af6195c8-1fcb-3455-a499-9494c55f090d | -13.50558 | -46.8353 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c8227f5-8b29-337a-a8d1-8c2006a1dc3d | -14.01797 | -44.55095 | 2025-08-30 05:57:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8809fb1e-e817-34e3-8e43-672ff3e42c5c | -11.58123 | -46.36417 | 2025-08-30 05:57:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 81cc33d7-5d9b-36c8-beb4-3e95d51b6f17 | -11.82409 | -46.46729 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6cefcaf4-e4b5-3a0f-88ea-fc36b288b6e9 | -13.38628 | -47.02483 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 1bfae96e-f706-3391-9477-0a4f735d435a | -11.84769 | -46.43206 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d57e37b9-5cff-3376-903c-dcf4b2c1cbc6 | -11.83182 | -46.47808 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 6b154656-7036-3696-89d0-a1b1cd9c7dda | -12.84615 | -48.17894 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e84ef121-0278-3cfd-a6a1-b2f8c9bd538b | -13.39728 | -46.9493 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ded424f-968f-3ef5-92fc-45cc15990266 | -13.36031 | -46.88549 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2baea319-568f-39f3-9c54-40b0df5793a3 | -13.67539 | -46.87288 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 438e1f44-6f5d-3170-ae39-49b264e3b65e | -12.01154 | -43.98888 | 2025-08-30 05:57:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 204.1 |
| 8fd14a8e-7ddb-354b-bd16-a7d25e20ea05 | -12.37129 | -46.39055 | 2025-08-30 05:57:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5ea0efcd-c77f-3f01-aead-8035982e38de | -16.98286 | -49.30338 | 2025-08-30 05:57:00 | AQUA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 045711e6-b217-361b-a2d2-596ebccb6a62 | -11.84636 | -46.44136 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9a2d04ff-6a2d-3971-b731-8b07ddc92e05 | -13.65934 | -46.91977 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85159da6-a796-3233-9eeb-1ec9103f5eee | -13.96402 | -46.32704 | 2025-08-30 05:57:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6461a732-0ea9-37cd-9331-cedfface9ff6 | -13.5351 | -46.9531 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 25fb866d-3eb2-37b8-b5ff-5fbc4242896b | -13.52604 | -46.95186 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 892b27a8-863b-3a55-8ab5-4dc8b105a5a7 | -11.92172 | -46.69037 | 2025-08-30 05:57:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 616a9a18-c8a0-37bb-9869-b1110417e76d | -11.8897 | -46.39849 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5fc9a11b-9854-3d2e-8eb0-7ffb6184a551 | -13.53646 | -46.94364 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd8a94c3-a8b0-3053-8977-4b8ea085860d | -11.15249 | -47.14759 | 2025-08-30 05:57:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d76d8a7b-8cba-3b09-9d2b-46f4af2bbb6d | -13.36061 | -47.01143 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 4473af31-3889-32df-b0ac-8de662712a92 | -13.37098 | -47.00336 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 028cc46e-8774-3720-8223-8c2b2730d376 | -13.68794 | -46.91407 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6fbb1a3b-3dcf-3ba5-be84-032353309260 | -13.52741 | -46.94236 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1745d9be-98e6-33d0-aacc-ee43eefbb435 | -10.03426 | -46.02766 | 2025-08-30 05:57:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 51c7a522-6a2c-31d9-9876-afe2c1ea53ac | -11.89106 | -46.38906 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 20f356f7-82c7-380c-a224-d79ea1ed20ab | 3.36694 | -61.22359 | 2025-08-30 05:57:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1fd3408-540e-3066-9c81-055fd97632b5 | -23.72355 | -51.75897 | 2025-08-30 05:59:00 | AQUA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| d36ca691-666e-35ba-8291-3099d4a48039 | -23.72203 | -51.76868 | 2025-08-30 05:59:00 | AQUA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 146.1 |
| fa317fe8-46f6-3eb0-a854-4de1b873b762 | 0.8902 | -60.43218 | 2025-08-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27209216-0593-34c7-802a-342d4a54465d | 0.89065 | -60.43502 | 2025-08-30 05:59:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe45f327-828b-318a-b84b-19e18cefea6f | -9.1155 | -65.7699 | 2025-08-30 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 9e5714cd-c7c0-326e-a7f1-ec5e1b08b88a | -13.3821 | -46.9924 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0b794378-5c19-3ed7-9a42-13ada7e9425e | -13.3649 | -46.882 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 7fa53070-3577-373e-8201-82769caf89a0 | -13.3825 | -46.9697 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b457cdd7-37c6-322d-8b13-47272fb36121 | -6.1853 | -43.3257 | 2025-08-30 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 268.6 |
| e8466c5c-8edf-3386-ae0e-451fae925356 | -11.8369 | -46.4514 | 2025-08-30 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1af03cc3-eb04-378a-a91e-680c69cd829c | -9.462 | -60.549 | 2025-08-30 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a5cb100b-4292-3f7e-a889-c4e2495aaee4 | -13.3817 | -47.015 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 6ecb6414-2ee8-3d73-bb77-6a3e8853e831 | -9.4497 | -62.3485 | 2025-08-30 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 248.6 |
| 91ce5775-8fb4-333d-a7b5-511a67c7f9a0 | -9.4683 | -62.3476 | 2025-08-30 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.9 |
| dae659c5-ed38-36a0-ae25-3024fa4e4d8c | -13.3843 | -46.879 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3ca45201-f6c4-3925-a8d0-4c7824957339 | -9.4498 | -62.3294 | 2025-08-30 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 292.4 |
| b7f88120-52f4-3dc9-9de4-e59ed9b024d3 | -6.1663 | -43.3506 | 2025-08-30 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ebcb066f-07ca-3a0e-8705-a4467d97b1ed | -13.3645 | -46.9047 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 99dfedfb-b634-3155-b163-b67c347c15e0 | -12.0153 | -43.9818 | 2025-08-30 06:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5a79246c-7e14-3635-a351-f0d22682c4e7 | -13.3628 | -46.9953 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| f0717004-57ad-3433-869d-5bd7718e8625 | -9.4433 | -60.5499 | 2025-08-30 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| e49fa869-269e-3073-bc55-c4a4eb92afce | -6.185 | -43.3491 | 2025-08-30 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 3d25692e-bb10-35ef-9ab9-c86e14cfe174 | -9.4684 | -62.3286 | 2025-08-30 06:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 166.0 |
| f928765b-a675-3240-a8d9-88e46659f6ec | -11.8365 | -46.4741 | 2025-08-30 06:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6f1d74cd-2f2f-3980-8fe1-cbfb011806b6 | -13.5373 | -46.9456 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0c698d18-381d-305c-ad7d-69393abc71e4 | -6.1665 | -43.3273 | 2025-08-30 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6fdc80db-46d1-3751-a44b-a4518dc9cf1f | -13.3623 | -47.018 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 709feb9b-a899-349e-998d-248a6391c830 | -12.0148 | -44.0054 | 2025-08-30 06:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ea133acd-55be-3abd-a060-36160508fef1 | -6.5263 | -44.8659 | 2025-08-30 06:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| af9af732-dcc0-3b27-a2dd-47b234f70962 | -13.518 | -46.9486 | 2025-08-30 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d595aec1-0521-3b3a-ba0e-cff6581902a2 | -9.4432 | -60.5692 | 2025-08-30 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b15a89f0-3038-346f-b665-6f7ec686180c | -28.7173 | -55.65226 | 2025-08-30 06:01:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.3 |
| 2237fb90-e699-3020-af1f-b29bf2afdc3b | -28.71958 | -55.63943 | 2025-08-30 06:01:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 31.7 |
| 364a8322-091e-3706-b8fe-259bb10ff8ff | -9.11867 | -65.76955 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33edd712-e3b8-3365-abdf-0fc5c0d2084e | -9.54439 | -65.69782 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 951b50f2-62fc-3b68-8cd5-47dd484565b8 | -9.46584 | -62.33905 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5f493146-8e3c-3dcd-a1cb-5cbca443e493 | -6.28193 | -68.22234 | 2025-08-30 06:01:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ecf0d8a-847a-35f8-a4bb-fdd7626afa99 | -9.11565 | -65.76181 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 49ab5c7b-17df-30a1-a7e2-6d9d2ae78dec | -8.46836 | -67.67665 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db65e242-ea9f-374b-8752-5865fd88dc48 | -11.30217 | -63.2554 | 2025-08-30 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff32ebe0-d005-3a6c-9241-a5e10331f25f | -9.44654 | -62.32698 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f539cf5a-c24d-35c0-928d-af65ac7f8017 | -8.62061 | -63.9519 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README80.md)
