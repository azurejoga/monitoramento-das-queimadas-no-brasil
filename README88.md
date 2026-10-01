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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1147050-8c10-3f57-ad76-7521c3226e32 | -4.306 | -50.74496 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 11772537-41ed-35db-8d25-a701f6052f29 | -3.68794 | -60.5393 | 2026-10-01 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ec7487-247a-3a78-a966-22c958da63bb | -4.26595 | -50.76376 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 1e284572-fa4f-3fd6-b4ab-b1e8d8d5951e | -3.29378 | -53.8606 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 71d23b94-857b-3e02-9cac-039198436d73 | -11.37963 | -55.12934 | 2026-10-01 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cd51007-7627-302a-851f-bc6e0f1b79b1 | -4.39226 | -54.83009 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe07d4a-0138-3888-a8ef-e593e196182d | -4.25149 | -50.75102 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 414d9be8-7d90-35ad-9c62-56d492a4deeb | -3.00856 | -53.88132 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e6adb51-f636-37e1-8097-766b1de51a3b | -4.0472 | -54.23119 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0921b923-4309-3e61-a715-de2fe4177e74 | -4.03712 | -54.23263 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43c60b01-78ca-36d5-85c4-737e307de61d | -4.30303 | -50.76651 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 4a514e10-e334-37dc-bf9b-784b7ce4989e | -9.00436 | -65.71262 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe8b059d-d8b9-31ef-b7c8-c43c66a75a22 | -4.26492 | -50.771 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| c428437d-00f5-306e-a8ff-6c35e966e767 | -4.29397 | -50.77531 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 19471738-dcc8-3fb4-a554-57d6a625164e | -9.0038 | -65.6946 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85562e8b-4719-31b6-9956-3746de30cf6a | -3.48999 | -59.53213 | 2026-10-01 05:55:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 300359da-14b6-3165-bae5-49aad28134db | -4.29914 | -50.79089 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| de381755-b305-3421-9615-9612081f81ef | -4.27319 | -50.76503 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 9079d137-8088-3692-970f-6e7876f55572 | -10.53607 | -57.77804 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bb6b780-faa4-3603-a89e-625834b0d584 | -4.05454 | -51.09969 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ec43331-014d-3999-8405-20676eee78f9 | -3.15874 | -54.0966 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f019d5d-c28f-3d86-86e3-e67f74af6efa | -3.17042 | -54.09847 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4c577aa6-b8ae-3b38-8471-4db0cd59bbd1 | -3.00895 | -54.22558 | 2026-10-01 05:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf0a4d8e-8af2-3733-9b2d-4eee879d3c35 | -4.04068 | -54.23486 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15a48e4e-a633-37ee-bb4e-b0852b610ca8 | -4.06658 | -51.09721 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68e1a1c2-fd19-3d5d-91db-aa8f511b19b1 | -3.98139 | -56.08503 | 2026-10-01 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6c7135-e980-371c-9fb7-2bc98ad76a14 | -12.7118 | -54.06303 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6193b956-bc53-3e80-8539-099ab4685cf5 | -4.14883 | -59.92009 | 2026-10-01 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4143310-8912-31b6-a169-61ebdf36c8ca | -4.30823 | -50.78257 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 170e8168-bdc6-39cb-b373-90443f00409f | -13.64415 | -53.93815 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd8cc711-2984-32a0-ade0-65677b89c84d | -3.01845 | -53.87592 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d784e87-246a-3665-b9a2-0d1b5439cf08 | -4.29872 | -50.74393 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 603a6257-20e4-3e8a-b1d6-1f41d5a6866b | -10.5306 | -57.78026 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87098ef9-8b77-3667-918b-ccd821ef5a27 | -3.02562 | -53.86821 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9c3c38-c08f-30aa-b381-bddcb4cf3148 | -4.05242 | -51.09474 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 980ee57e-4ba7-3646-93ac-fb846681123a | -9.78141 | -59.01652 | 2026-10-01 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c356c99-21b6-35a1-a774-f3925f266aea | -10.53257 | -57.7654 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb69f792-e997-3fd8-a0dd-ed3efec83126 | -13.66376 | -53.94669 | 2026-10-01 05:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7f66a5a-e224-348a-9898-3d4441f7f842 | -3.01658 | -53.88876 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 638e2956-1b5f-3943-b22d-650381a6bc01 | -4.26485 | -59.88959 | 2026-10-01 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5c08033-563a-3775-8864-e6a275d2a785 | -9.74673 | -65.05045 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efb56cfe-a49b-34e8-af77-e432293412e3 | -9.00491 | -65.70912 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11459ede-4ad9-385b-85ef-e59705c13c1c | -4.32265 | -50.73206 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6c5987-76bc-382f-836d-f2d42197dfce | -4.04303 | -54.23325 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6787b4b5-4e54-376d-8322-e1f199d1eff0 | -4.03653 | -54.23652 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77b6d7ed-4356-35b7-8dc8-af6be2a05558 | -4.27738 | -50.73559 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9b81bbd-c2f9-3163-8d13-9dc93c4ef2fa | -9.78077 | -59.02123 | 2026-10-01 05:55:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d41c7d2-5ce1-32cb-9591-75779dda8c08 | -3.17231 | -54.08593 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84387fe3-c816-3c80-b883-08adfd8f1118 | -9.35037 | -57.16555 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88c93102-e8ac-3d72-9186-9a36e7e71f02 | -3.11106 | -60.6789 | 2026-10-01 05:55:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e915279-9832-3e82-80d1-29e098676532 | -4.07879 | -54.87384 | 2026-10-01 05:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52d01804-1a21-3e14-9b21-aaa1089769a5 | -4.25873 | -50.76234 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| eebfc3a1-5f79-3f86-8df9-756a8d3f511b | -4.39157 | -54.82352 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0e21845-ce9f-3ca9-94f9-f137158678f2 | -4.06166 | -51.10064 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79d30f14-c797-3003-8bb1-6a8f7e03f838 | -4.04185 | -54.22668 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be0816b6-6f2e-3ade-bc54-c8a84dbaaa10 | -4.29372 | -50.78032 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a605cd56-b831-314a-898c-c59aa90b0d97 | -3.00922 | -53.87701 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21959019-76f3-32ac-912b-16991dccafbc | -11.38074 | -55.12008 | 2026-10-01 05:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d648a258-5b82-3977-a66b-b42aac864a0a | -4.29729 | -54.79379 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15741f4-a548-322f-be70-6d0240af84b5 | -4.31488 | -50.73338 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 837cfe4c-2243-3cf9-b9a9-d217553c1715 | -4.2743 | -50.75721 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c6cf00c6-aacd-3e52-9130-edf27bbde670 | -9.31547 | -57.71145 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c435f59c-d32b-30bd-a752-8928396dddb3 | -4.30439 | -50.75454 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8daa0894-e2b0-31fe-90ba-0cabab5dc6bb | -4.04427 | -54.22501 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308795ad-365f-3b5c-bd61-29500b05df34 | -9.00602 | -65.70213 | 2026-10-01 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d934d5e-6e74-35b8-bb8e-056711640378 | -3.01254 | -53.87493 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19eb14cc-0b00-329a-818a-636f94804735 | -12.70119 | -54.06791 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4994f9a-ecf3-33a9-a7ca-3fa619f594e9 | -4.05859 | -51.10221 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60e95acf-86ea-3198-b1d1-9603e4d67027 | -10.51653 | -57.7691 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3432b54-ba0e-31da-89a5-a60cafcf4b29 | -10.53766 | -57.76611 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f42bccd-c316-36d9-9160-462d21ef371e | -3.98658 | -56.08577 | 2026-10-01 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ca5da56-a633-32cc-889a-ae2da9dd87bc | -3.01128 | -53.88358 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb84d661-eec5-33dd-b74b-b6a989aa90a4 | -4.24425 | -50.74973 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b5f68ac-bce5-385d-b7bd-e34510409e01 | -3.02897 | -53.86673 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bdb90fa-626d-3356-ae8c-543f9dee06d7 | -9.34347 | -57.17723 | 2026-10-01 05:55:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4081a8cf-0c73-38aa-84e8-651c36975f06 | -12.77745 | -54.01806 | 2026-10-01 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6004da07-be20-3502-af45-b620f6588362 | -3.18164 | -60.06406 | 2026-10-01 05:55:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5144f758-36d4-3485-990c-822328313c18 | -4.3085 | -50.7774 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ad2156f-55e0-311d-8aa5-fd174dd7c7bc | -3.59344 | -54.55083 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69bc9346-6dc3-3225-814d-7a6f5e59111c | -4.05546 | -51.09311 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5b96e2c-9438-32e9-8e64-3cc2d27d1466 | -4.39281 | -54.82625 | 2026-10-01 05:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6f9733-401e-3c17-980b-5d114ad3c3c1 | -3.15602 | -54.07473 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93a8f7d6-e568-30ae-9cb4-d341b21b904d | -3.7679 | -58.83951 | 2026-10-01 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 066c37c1-c49f-30a8-97d1-62125e81762e | -4.28987 | -50.75216 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 22e9f63d-d395-3c99-9dd0-80cda749509a | -4.25767 | -50.75941 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 11869bf8-60e9-3c6f-ac01-056b1494bf63 | -3.18154 | -54.10406 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cbbdcbaa-08f5-3534-a34b-460d3271f22e | -4.25255 | -50.74381 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| eb85cfb0-f0d7-3452-9ad3-8e96738dcfc3 | -3.28912 | -53.85103 | 2026-10-01 05:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c813f9f4-c5eb-35a6-9745-c23a4b601c5a | -9.74337 | -65.04992 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71ecd2e5-32e8-3611-878d-62f194664378 | -4.0657 | -51.10321 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a000af14-0721-39d0-8d9a-bb9e23e559ec | -10.46408 | -59.13058 | 2026-10-01 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ae4a190-8901-303d-bdb8-900f7bbc1590 | -10.54625 | -57.77945 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a7d823-cd74-35e5-9a8c-f0214a004a01 | -4.29192 | -50.73787 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b53acfc8-73b7-3cad-b5b7-4df53e04671b | -3.71713 | -58.79936 | 2026-10-01 05:55:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5ea9272-ab78-3239-b971-a5aa380e2e2e | -9.88563 | -65.14174 | 2026-10-01 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90b91828-9864-33ca-88fa-37b2d8552509 | -4.2691 | -50.74159 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5ba84a33-a10c-3555-89b4-12d95194af8e | -4.29612 | -50.76036 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9bd07bd8-91dc-3b86-89d6-45fd9c506e86 | -10.53529 | -57.78389 | 2026-10-01 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ceb7d8af-0136-3cbd-952f-5bcfb2131fb7 | -4.24632 | -50.74512 | 2026-10-01 05:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5dbbcc4c-ae5b-328b-905a-421976e4bc9f | -4.30025 | -50.73167 | 2026-10-01 05:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README89.md)
