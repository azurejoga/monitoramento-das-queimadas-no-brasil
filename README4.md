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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2312a65-00ed-35ed-8047-e6afec3a67e8 | -15.0742 | -48.385399 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 990970fc-829d-337c-a5c4-837eff94a852 | -10.0247 | -51.101898 | 2025-08-29 00:31:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95f6c027-4665-3682-8a64-8affa9bc9ef0 | -13.5592 | -46.921101 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b85f4759-3c7e-343c-a637-9e597a7862dc | -13.3737 | -46.869801 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c19c4b2-52d2-3e48-82c6-56f1017ff4a1 | -6.4758 | -50.201 | 2025-08-29 00:31:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6612026b-3763-3056-9f5e-694be1ef115c | -11.0967 | -44.764198 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a5da83a-558c-38db-8740-9f1cd9d8a151 | -9.4348 | -47.645699 | 2025-08-29 00:31:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d98b89c4-f98e-3102-a65d-da3c3b3db1db | -6.7357 | -43.5746 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99f4fd5a-b3c5-3854-987a-ec3d759baf5d | -7.0612 | -44.353001 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5709569c-a2d6-3fda-9580-3be035ee86ec | -15.1315 | -48.1175 | 2025-08-29 00:31:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf4c765b-1a58-3da0-9c8b-d3d46cfeabfc | -3.4223 | -49.049301 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0975ef6-4fb2-3dbe-83c1-f2d53a970ff2 | -7.2442 | -45.4165 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2863cc1-7591-391c-aa18-b4316c9718b0 | -5.1265 | -43.2253 | 2025-08-29 00:31:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8b22cee-f0c6-3dc2-a5a6-fa7ac6961fe9 | -10.6477 | -48.6427 | 2025-08-29 00:31:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1f85902-7545-301e-9768-18feab00f1ae | -11.3251 | -43.553799 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6b6bdd2-82ad-3b9a-98f0-4583f8b19639 | -3.4206 | -49.0415 | 2025-08-29 00:31:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f41723cd-ddd1-35a1-918b-03759600e316 | -3.9864 | -43.247101 | 2025-08-29 00:31:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5588799-fc00-325f-93fb-5991b3d86f8a | -11.7886 | -44.678398 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80227224-f88c-3cf2-bc73-3c835c831bc2 | -13.0905 | -43.062302 | 2025-08-29 00:31:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7c510f36-d6e0-38f3-a7ef-8f24e0c57b0e | -5.7991 | -42.573898 | 2025-08-29 00:31:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c6844cb-1617-321f-8103-9ca0443e4fad | -7.2195 | -45.443802 | 2025-08-29 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5f5fc30-a643-3b09-a522-091210f5b858 | -13.5569 | -46.8629 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25eaa653-448c-30de-8cc7-38a3aa1d0702 | -13.5511 | -46.9314 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 87c8c310-29ec-3027-abef-075da6dbe63f | -11.4681 | -47.313999 | 2025-08-29 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4923d4d5-4f84-30ff-b849-fe0b41929a75 | -8.7063 | -50.377102 | 2025-08-29 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0833e798-873a-3b7c-a55a-9a16fed58bcc | -13.6801 | -46.9114 | 2025-08-29 00:31:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e234bf1-679d-31b5-bbee-450bb84f503d | -3.4561 | -44.292702 | 2025-08-29 00:31:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04af04c4-1c34-3c74-822f-98ef624f8a41 | -7.2304 | -45.311298 | 2025-08-29 00:31:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a88fcd62-02e2-39d9-baf4-57d9ee2e8e6d | -11.96 | -44.844002 | 2025-08-29 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cadca7ca-09a1-3494-b78d-0108ecc0816c | -22.6761 | -46.845402 | 2025-08-29 00:31:00 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42559e8c-e2d2-3d6f-809c-145d492ad0e0 | -3.747 | -48.937199 | 2025-08-29 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96a63465-a435-392b-88ac-47b56197261b | -6.5439 | -43.1077 | 2025-08-29 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d091e726-186a-3fb1-8a10-a95bd0c45b48 | -6.7098 | -49.4482 | 2025-08-29 00:31:00 | METOP-C | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5508aa86-6ab0-3fa6-8737-07db7c2d329a | -6.8806 | -43.620201 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 31f3b8ff-f485-371d-be03-e27d739cab26 | -11.5899 | -46.3694 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80d2cd1a-29eb-3624-860a-cf6233941b03 | -17.3514 | -42.646999 | 2025-08-29 00:31:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 80654ede-63c9-30f7-b8f1-7db623039f54 | -13.6703 | -46.913502 | 2025-08-29 00:31:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9643a07b-9d0b-3d68-89c9-2414ea1afd23 | -12.7144 | -48.150501 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 981e75fb-9e45-3a97-adbe-53c7da82edd3 | -3.7659 | -54.793999 | 2025-08-29 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53209c8e-bcf9-39e0-92d3-2ffde5505b13 | -5.7971 | -42.565399 | 2025-08-29 00:31:00 | METOP-C | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71106923-0ded-3356-9642-cbe07996c997 | -11.3219 | -43.584599 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b2411cc-f87d-3304-b28b-f33a189a5977 | -11.243 | -45.000702 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3755e0-1495-3340-9743-3d842287e5bc | -13.4093 | -46.987801 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4ccebc33-0374-39cd-bc20-99eca2f2b803 | -5.6977 | -45.959702 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b17e4a0-f126-37ef-baff-d245c3cf85a4 | -8.4952 | -43.682201 | 2025-08-29 00:31:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d42ec6e0-fd53-3d00-abf5-7c5f72c2d087 | -12.8218 | -48.174301 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 946eb883-b659-3c05-8ea0-8ffd4131ffd9 | -9.495 | -45.3839 | 2025-08-29 00:31:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4d134aa-5848-3c39-b353-41e399e0220e | -7.4025 | -45.929001 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9ecb2b8-56aa-3c21-95ec-77b08bbd0872 | -9.4429 | -47.6357 | 2025-08-29 00:31:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32868a37-ca90-32cd-a854-b17ddd4c8f14 | -7.6398 | -42.718601 | 2025-08-29 00:31:00 | METOP-C | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2251fde9-44fc-30b6-90e1-80cb75f5c0cd | -17.051701 | -45.886799 | 2025-08-29 00:31:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef0f819-28f2-300e-94b3-d66cc085da6c | -8.4458 | -43.647499 | 2025-08-29 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 868aaa4f-48f0-3278-8ed5-458ea95dbaa8 | -14.0094 | -46.3433 | 2025-08-29 00:31:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73f6850f-6e38-35d8-ad8d-7f7acdcb36e7 | -17.608299 | -46.690701 | 2025-08-29 00:31:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a628aa1f-687d-37b8-9cc3-3f419cb2bc07 | -5.6231 | -45.006599 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8b880b-faa0-35cd-ae1e-83f5ad381f31 | -12.7046 | -48.152599 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11293459-f6f1-3667-85f5-c15e80ccd607 | -9.8499 | -44.678299 | 2025-08-29 00:31:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef6c886d-44b1-34b5-885b-e88593bc8ad5 | -6.5486 | -43.923199 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7533ed8-70fe-343b-b847-8a715b2a0f87 | -7.7314 | -50.271301 | 2025-08-29 00:31:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59ffd31f-7a00-3a94-8a3e-f3c0bd450677 | -5.6329 | -45.004398 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45975633-3c35-3b85-9da9-9821c168c722 | -21.1052 | -42.138802 | 2025-08-29 00:31:00 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd694880-2e5f-3c53-81bb-3ed507d224ab | -3.9868 | -47.951199 | 2025-08-29 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 254d0e0d-443c-37de-8c00-866c50e8b3bb | -11.0306 | -45.063801 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| deb28b5e-7221-36c2-91c8-83c71f0609d4 | -11.0869 | -44.766399 | 2025-08-29 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f73aa9e-fd54-327a-b5ed-a7cf5c8afc86 | -13.5862 | -46.8564 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d86da374-14ae-3da2-9573-7d80e4c05fce | -8.6966 | -50.3792 | 2025-08-29 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9db85e19-269b-33da-8c44-066be7fba380 | -13.5638 | -46.894901 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0838db0b-827f-39cb-aab6-2fac35dea410 | -11.3317 | -43.582298 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b964ee39-8fdf-399e-8fce-b35e49f2ed8a | -13.4335 | -46.957199 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 618de712-06f3-3356-8fd6-a77f79b14b0c | -13.5011 | -46.841801 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eae0a04e-d11b-3901-b584-af0b4d6d6fa8 | -6.6495 | -43.5149 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32084f19-6224-3cab-9107-46a14a0a8a73 | -11.3496 | -43.5257 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b641c78-2d39-3a34-a924-28409fba0683 | -6.211 | -43.008801 | 2025-08-29 00:31:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c84615b-7112-3a50-90fa-d5d340b3c4e0 | -11.3594 | -43.568401 | 2025-08-29 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f319b47-5e7b-3e77-9862-16f6472cca1f | -6.7339 | -43.567101 | 2025-08-29 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb1078c2-20c2-3592-a32a-86a7b4b0f6fb | -12.0441 | -50.618198 | 2025-08-29 00:31:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb4bc10d-7bc2-3036-bc10-b0c7d870308e | -11.0322 | -45.070801 | 2025-08-29 00:31:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 884221d1-4f18-390f-9317-9d8c574ba74a | -7.0547 | -44.369499 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd1d5f71-aecf-3ef0-b4d7-b1c8d6aa7517 | -13.1891 | -45.273201 | 2025-08-29 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78544519-c37e-3254-92eb-741772c67ac3 | -5.8683 | -38.273201 | 2025-08-29 00:31:00 | METOP-C | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8fd57e56-7395-3651-8acd-36709939a1b2 | -13.4433 | -46.955101 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5b34d62-c018-3967-913e-48790caac87f | -7.404 | -45.935902 | 2025-08-29 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce6d26d-1953-369e-ab13-05322a82e8ac | -11.6013 | -46.3745 | 2025-08-29 00:31:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79ee36f9-74ac-37c6-87ef-2f18db3001d2 | -13.5764 | -46.858601 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4bd3e53e-e183-365b-b53e-6ce8797337c6 | -10.8513 | -47.499298 | 2025-08-29 00:31:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c047c7f5-3679-3846-9c33-c6754d8dc91a | -14.4188 | -42.8675 | 2025-08-29 00:31:00 | METOP-C | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2803e678-8126-31d5-881e-2a1239eb1417 | -5.6215 | -44.999699 | 2025-08-29 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37d1594f-e1c4-3bce-bc7c-965d49ed5aed | -19.1705 | -46.582699 | 2025-08-29 00:31:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa97c549-e8c9-3391-8139-ff8a7bcc3485 | -6.7988 | -43.756802 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e4cebdc-2402-3685-87ba-d37e570eb857 | -12.7163 | -48.1595 | 2025-08-29 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4bf2e6-e16b-3d73-a733-719a5367eb8c | -11.577 | -46.264599 | 2025-08-29 00:31:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e32f05f-d190-38d5-bbbe-3deb74ef7bc4 | -11.2394 | -44.123699 | 2025-08-29 00:31:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0207c96-17ff-36ef-9b10-9d14e27f92dd | -13.4128 | -47.004002 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2f8ec83a-5087-31ba-bed4-6800a198b732 | -13.5143 | -46.855598 | 2025-08-29 00:31:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ce457e2-a723-38b9-90bb-d74a45357c5a | -5.1861 | -46.067501 | 2025-08-29 00:31:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9cbde2-c6b8-3a0c-a887-6f506702f0eb | -6.8771 | -43.605301 | 2025-08-29 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e39e3418-43a7-3969-95f4-05f6e52adf8b | -6.5601 | -43.928299 | 2025-08-29 00:31:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ada002f-2985-3da5-a217-8f7df0d34109 | -7.0498 | -44.348202 | 2025-08-29 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab402085-3a7e-35c9-b37c-95046027266f | -5.7059 | -45.950699 | 2025-08-29 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af01b1e2-7eb5-3f72-a48e-6659c10670ca | -17.0403 | -45.880901 | 2025-08-29 00:31:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
