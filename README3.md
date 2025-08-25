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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdb4d359-3ed8-3d3f-9827-fcebe909c0a4 | -7.8416 | -49.988098 | 2025-08-25 00:14:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a231ea2-a6eb-3cb1-bdde-5ecda8a64fea | -6.4894 | -43.428299 | 2025-08-25 00:14:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e62dfba-abce-3468-baa1-5fd01e59fcf9 | -10.7233 | -47.135399 | 2025-08-25 00:14:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06ec8a8c-5123-3bde-a757-d1d143d04f5f | -10.7108 | -47.123901 | 2025-08-25 00:14:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a140afb2-f13f-36b4-a1f8-600bb293d0d1 | -3.4526 | -43.3465 | 2025-08-25 00:14:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21e376c5-2752-39e3-b083-9de312d1494d | -3.4422 | -49.043201 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a70d180-c5c8-3383-969c-4e6929cebb25 | -14.5769 | -45.723801 | 2025-08-25 00:14:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a19af462-83cb-35c0-8715-19d760062085 | -19.5732 | -41.611198 | 2025-08-25 00:14:00 | METOP-C | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1550dd41-4854-338d-8906-884f78b1e873 | -8.1783 | -45.066799 | 2025-08-25 00:14:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4799a20b-6dcd-3abe-9d54-24072ef8ae02 | -3.4324 | -49.0453 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a2c9052-5853-3f7c-892d-9137cea2159b | -6.0282 | -44.2164 | 2025-08-25 00:14:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fedcc800-6c7f-300e-9e7b-fdf24d60b798 | -8.3849 | -47.979599 | 2025-08-25 00:14:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bef1c87-04e5-3b62-a8a4-ae55b87b7748 | -5.1031 | -43.217499 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a38d77a-acda-34f5-8e4e-27e1b9dc5a47 | -12.7488 | -48.1222 | 2025-08-25 00:14:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbc11560-96d3-36c5-96c9-e40fa1899480 | -11.1942 | -48.449799 | 2025-08-25 00:14:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9a00aff-2125-3e91-bf91-63aee8966165 | -7.2027 | -49.603802 | 2025-08-25 00:14:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24202544-fbee-3d34-a16d-6c461d94bb5c | -15.707 | -41.93 | 2025-08-25 00:14:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53f203af-c58a-3416-89b9-2bee0f6794df | -4.6752 | -41.0299 | 2025-08-25 00:14:00 | METOP-C | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5ef97e56-ed5d-3191-8611-48d2b07a672d | -6.435 | -44.564899 | 2025-08-25 00:14:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38e2ab5d-7362-3495-afef-fa883c5504f2 | -5.485 | -41.411098 | 2025-08-25 00:14:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aab63d78-b837-36fe-9562-399b3dbe7794 | -6.1296 | -44.3936 | 2025-08-25 00:14:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47b78c98-199a-3550-a9b0-51dcb8035aaa | -6.1408 | -43.1604 | 2025-08-25 00:14:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 0f8521c0-db77-348b-952d-100b1b204627 | -8.5473 | -48.849201 | 2025-08-25 00:14:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc39d58-b203-388c-8c8d-f49775dd66e7 | -6.2624 | -42.877899 | 2025-08-25 00:14:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6659bb3-e30a-352f-b949-7593caffe989 | -5.296 | -45.263901 | 2025-08-25 00:14:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf7ff056-a655-3fc9-90b4-ac45592b6c3d | -8.0688 | -49.668499 | 2025-08-25 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0212424-6f73-3699-b690-4d49caedb76d | -8.5439 | -48.832901 | 2025-08-25 00:14:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1686decf-0e65-301a-83f7-2c6516b57717 | -5.4964 | -41.415699 | 2025-08-25 00:14:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4fa82f3d-d07d-395c-b43f-8002b027ea86 | -11.6454 | -46.225399 | 2025-08-25 00:14:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84c5fe21-841b-3026-a2b0-ed41eaa28748 | -13.2186 | -43.148499 | 2025-08-25 00:14:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8a57183d-18f8-360a-ab0c-58c00bb9d86d | -10.7177 | -47.108501 | 2025-08-25 00:14:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c3991f43-5ad1-3b18-8c0f-20277f756d26 | -19.8169 | -42.212299 | 2025-08-25 00:14:00 | METOP-C | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b00decb-f20c-39d8-b972-025c92a2b16d | -3.4227 | -49.047401 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7250124-42e1-3148-9809-5a0deb06793a | -4.17 | -40.718498 | 2025-08-25 00:14:00 | METOP-C | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 50d3cc31-3754-35f4-bc35-0da8accdc4da | -5.1211 | -43.206001 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3eb08a1-7fdb-3d76-9088-33c386725e29 | -6.6815 | -44.425201 | 2025-08-25 00:14:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7d7dcd3-ee42-3d03-9cba-ebe16d406b94 | -8.5375 | -48.8512 | 2025-08-25 00:14:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ef3e2095-ef29-3768-8c6a-1c1b10445692 | -6.6797 | -44.417099 | 2025-08-25 00:14:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a01c5d12-4333-3489-aece-8e6e9ad771aa | -12.7606 | -44.421101 | 2025-08-25 00:14:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5790abbe-1d33-3366-875b-2c71e50092c9 | -8.5507 | -48.865601 | 2025-08-25 00:14:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 2792e2c1-c3ae-379e-9226-c5760a64b578 | -4.6575 | -43.115601 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0d98b8f-6da6-39fe-856c-cd0973389962 | -8.5341 | -48.8349 | 2025-08-25 00:14:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7a5899-e138-32fb-91c7-e037f3c73b2c | -13.4424 | -46.9146 | 2025-08-25 00:14:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efe93da7-402b-3c29-9862-efdafd7781a3 | -7.5364 | -46.0247 | 2025-08-25 00:14:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1607669a-e7a4-3db3-85c9-d5b25e8793e9 | -11.5972 | -46.337299 | 2025-08-25 00:14:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cebeee3-66f7-39b4-8b35-ef1fe54fde98 | -5.0999 | -43.2033 | 2025-08-25 00:14:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 644a0f25-aaba-3226-9532-9ab2347ac13a | -13.4494 | -46.898201 | 2025-08-25 00:14:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d858e3a-c781-3145-9b52-dfa629d22e33 | -14.3832 | -51.938202 | 2025-08-25 00:14:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3f0c5354-0241-379d-b35f-fdcd0067139c | -7.816 | -46.891102 | 2025-08-25 00:14:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b745d56-d353-346a-86fd-99d76fac4a6f | -5.7295 | -46.1516 | 2025-08-25 00:14:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cbf59d1d-ebfe-3cdf-b1f9-69c04eb14dc3 | -6.7022 | -44.010899 | 2025-08-25 00:14:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcec99cf-1628-3f04-857a-e582ba471478 | -3.4196 | -49.033401 | 2025-08-25 00:14:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70faf488-3c3d-337d-86b5-1d0a3dbd78c8 | -15.0521 | -43.841801 | 2025-08-25 00:14:00 | METOP-C | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| f9435cb8-1e43-316d-9466-d86df19a4f38 | -17.837099 | -40.130402 | 2025-08-25 00:14:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97c96532-4976-3346-bb57-d997ffc45de9 | -13.4522 | -46.912601 | 2025-08-25 00:14:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bbda00ac-2e53-3ae1-88bb-1aa6af2a771f | -10.6011 | -44.326099 | 2025-08-25 00:14:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50b9fcb7-222e-3d96-aa40-a450d53b8a53 | -8.3879 | -47.993698 | 2025-08-25 00:14:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a77e31b-6170-35a2-8dab-d2d270b6be97 | -8.0591 | -49.670502 | 2025-08-25 00:14:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ca507d-b4db-3b74-a827-6fba8636c556 | -10.0319 | -45.3013 | 2025-08-25 00:14:00 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 756b14b8-3d86-3557-9948-edbad5ace1b6 | -8.8918 | -62.4677 | 2025-08-25 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 07a34d7a-563c-322b-aeb6-30ee4d3bc648 | -6.782 | -59.6519 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.4 |
| ba1abe1d-3e59-3d7d-aaac-9837471482a7 | -10.0232 | -51.0712 | 2025-08-25 00:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4d9b35e0-ddb9-3b0e-abf0-665f979c4196 | -5.118 | -43.2198 | 2025-08-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| edd30d18-ebce-352f-8032-67de0749bd36 | -6.8202 | -59.4194 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 99cdd22e-d247-3b30-9f48-d85a409501db | -8.8919 | -62.4487 | 2025-08-25 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| cf404bf6-fef2-3d11-a986-c76ef177d9a2 | -8.8734 | -62.4495 | 2025-08-25 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 736a5fbb-4481-350c-bb53-7f29dac3198e | -9.8101 | -64.2642 | 2025-08-25 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0bb6c80d-33a3-3e07-9f5b-1fb92c12b009 | -6.7635 | -59.6718 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 7ae957ec-63f1-356e-8606-b7544d932dc1 | -6.7821 | -59.6326 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c49b18f6-31c5-35ee-ba5a-f7787f34a9b7 | -10.5937 | -44.331 | 2025-08-25 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2ff2d84d-2c7d-3688-966c-4499a522da7b | -5.0994 | -43.1977 | 2025-08-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5c36a595-0737-38a0-9df7-b03a87695a48 | -3.4254 | -49.0517 | 2025-08-25 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| a40303c1-ab7c-3b1f-9ae0-b6a5e1f9bdd9 | -9.1909 | -59.4619 | 2025-08-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 971328b7-5292-36c8-ac15-e3e238bf8979 | -5.3078 | -60.2008 | 2025-08-25 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 601545c4-8ade-3025-a9a4-8938dea98365 | -7.6326 | -62.7243 | 2025-08-25 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 73b34bda-af3c-31fa-a552-7149d6ecdd6b | -18.0799 | -51.3908 | 2025-08-25 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2fe0daa2-ca31-34b6-a357-b49c0f43d823 | -6.7819 | -59.6711 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.7 |
| b7c0efe0-4d3a-35c8-b8ad-a43613fec5c7 | -9.1988 | -60.9274 | 2025-08-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b45f6c9b-e9fa-358f-a673-8499af57e365 | -6.8004 | -59.6704 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| db9da056-3873-30ec-b98c-6053651f652e | -9.2174 | -60.9265 | 2025-08-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 35b5e515-eddb-3c51-81eb-2f808cf146eb | -7.6141 | -62.7249 | 2025-08-25 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a1953992-e041-3b6f-8071-ad0c94df1ac0 | -6.7636 | -59.6526 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 81baabc8-4d8b-365a-82ea-deeb1bdf660c | -5.0992 | -43.2211 | 2025-08-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 93c0b495-728d-3ae4-8195-e3f5b09112ca | -5.1181 | -43.1964 | 2025-08-25 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| a44ca58c-359c-38be-8b42-c47fc7787207 | -5.4364 | -60.1779 | 2025-08-25 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 11ee3ea5-a861-3f08-847e-26f6d51b3110 | -8.1119 | -62.877 | 2025-08-25 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 6c22832d-382a-3df4-80c3-3129ab797994 | -8.8733 | -62.4685 | 2025-08-25 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 52b7afcf-ac76-3c81-a86b-07a22ead5a63 | -8.5458 | -48.8592 | 2025-08-25 00:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a0aec112-f2fc-3942-a5f3-b4f15f10ef25 | -8.2128 | -61.393 | 2025-08-25 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| d4f775aa-5c07-3426-8ddf-505a075f0b62 | -8.2313 | -61.3922 | 2025-08-25 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f3cf0a74-a8c6-348a-8b44-695a29547003 | -5.4181 | -60.1784 | 2025-08-25 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| f5a07822-b961-3cc3-9409-863779b958fc | -6.8201 | -59.4386 | 2025-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 54d9f6a9-5466-329b-a3f5-2b868b61888b | -9.1722 | -59.4629 | 2025-08-25 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e50518a2-4726-3579-8843-aa4a044b4b46 | -3.4439 | -49.051 | 2025-08-25 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| cb56f036-1e90-3c16-b532-712df446fca1 | -18.4294 | -49.1948 | 2025-08-25 00:30:00 | GOES-19 | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 79d98223-dc12-3413-af7d-d8fbc9e63707 | -8.2313 | -61.3922 | 2025-08-25 00:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d13ecbbd-4a02-37c4-b4fa-41e4364b65bb | -9.0061 | -65.3813 | 2025-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a52e9c33-9dba-3da4-80a2-ace2632966de | -12.7576 | -44.402 | 2025-08-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| de64bef2-273d-3544-ba90-32cf0da45479 | -9.8101 | -64.2642 | 2025-08-25 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 252c35ad-c3bd-338d-9639-2ff0ee037657 | -9.8287 | -64.2635 | 2025-08-25 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |


[Clique aqui para ver as próximas entradas](README4.md)
