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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77042232-a049-3ce3-8882-34c3ac780981 | -10.97993 | -46.84917 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9f947da-5c80-3ce2-9080-01b206ab3c1b | -10.98379 | -46.84618 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41c5a48b-fa69-3fcd-a38f-c934cf39ebc7 | -11.64432 | -52.21319 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c5cb1b1-5810-3a5d-b9d5-9c36d3b00685 | -12.46389 | -48.08491 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7579871-dba0-3fe6-bf6a-8b307a43befd | -10.14346 | -46.25436 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa4e690-7750-3849-b8b1-a254deb24c92 | -14.53869 | -48.06279 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 20b71a0d-257e-3aca-8992-41b2fc10b6d9 | -10.58152 | -55.41309 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4be1bad8-b919-33c6-8237-b03caa078128 | -10.48816 | -46.77459 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e5e433-989f-3db8-8ec2-fb12e91cecdb | -11.58948 | -47.76218 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27133cc9-75d8-3f35-b5fa-e334110a5e9c | -10.11619 | -46.23183 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 451c8765-c830-3a87-8ce9-b74a60b265e4 | -15.04646 | -50.03983 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61364f52-ec78-3596-b809-bbf70188b3d7 | -14.60116 | -48.01178 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 61338dad-4344-324d-aa98-edc7d74d14eb | -14.29005 | -45.22892 | 2025-09-04 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff6af22a-5fe1-3a9e-9c33-0d26f49db005 | -10.44923 | -53.61774 | 2025-09-04 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 240aa009-9233-358d-ac7f-a08d067e1683 | -14.28708 | -45.22421 | 2025-09-04 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e764b08-7e06-3f93-8027-7de9f2f8ce7f | -10.73551 | -49.59431 | 2025-09-04 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04d25f4e-4e02-316a-8a69-b8339ec77953 | -6.74853 | -58.72606 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f86bfd9e-1c19-3aa1-8bf2-a9b9b1fd3f0a | -12.23647 | -50.15322 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55851a5a-6f94-3a90-a407-7d4905577dd4 | -7.36836 | -49.39457 | 2025-09-04 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 196cdd2e-a992-3484-9efa-1e59c932a505 | -13.57637 | -48.12623 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a56f2f2-70a1-32d7-b697-c2b6bb8a2de4 | -10.43605 | -50.3891 | 2025-09-04 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7176b73-788b-3919-9bde-ea75af10b418 | -8.52674 | -51.31593 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3443bf25-3684-321c-90c0-c591ae898800 | -12.9672 | -54.76907 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a76b7256-d990-3e73-a6c6-6878dfe9995d | -11.58857 | -52.15913 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d96f1da-edc8-3e61-962d-20929822c2ba | -7.97426 | -46.34168 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 865f48f1-2afb-349e-ac7c-e62f0b044512 | -8.73182 | -47.00185 | 2025-09-04 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1a83172-07a0-3ffa-bbf9-b7ed4e9d8183 | -11.84514 | -51.44472 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5047834b-383d-3b95-a7d3-d139127f1724 | -13.94928 | -53.98597 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc34cbb9-ed5d-3068-86ef-d929f1f5dda4 | -13.44475 | -46.92911 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0644fd0b-7bb8-363a-ba1b-67a3a93f2cb7 | -11.88854 | -51.53833 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cc81629-56f9-3358-a369-bd1ef34ec102 | -9.61362 | -47.03975 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ce8873b0-d6c5-3ec1-899d-f500ecd3c4a1 | -9.81034 | -45.98679 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c714aea9-7440-3060-85e7-5729b73d7012 | -14.75197 | -48.13438 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a09abb7d-8407-3268-92e6-0cc43b5dd2be | -6.67296 | -60.03088 | 2025-09-04 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5090f791-b64c-3aaa-8cae-552cefe6cf41 | -11.05084 | -45.40705 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 325551c9-020e-3d15-b149-0e7efdf10ff8 | -8.73623 | -47.53753 | 2025-09-04 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d0e429b-c81c-3dfe-ae1d-6fcb0b4c7a9b | -12.8819 | -48.02321 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51b7f5fe-d596-35ac-a785-3b0954d5ba4c | -9.59948 | -47.84524 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30951315-a1ed-3db5-804a-8b2d9921e0f1 | -11.7347 | -47.74658 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33a1a561-1199-37fa-b2a9-4ff0d984ed5b | -14.19825 | -48.08694 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da08b6c5-158b-3558-bc5d-22d896b88e80 | -8.20284 | -44.79235 | 2025-09-04 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e34d7427-6a07-31e4-8225-c0de51fa618e | -15.04796 | -50.0518 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b99daed-dad4-3bc3-9c70-af47dcc6d9ad | -11.58456 | -52.11252 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f2564106-21a7-3c07-982b-f928969d01f2 | -9.48607 | -47.61528 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e0dec06-1020-3ac2-a904-f1cafb8e9a3c | -14.77984 | -48.13158 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b7bf5b0-08a5-3f36-9dfb-57e33495fd3b | -12.94617 | -48.07023 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 850e87ba-5aa4-3c17-9842-68090a39be24 | -15.04709 | -50.03602 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 673ea239-7afe-3829-92ff-1114a705ec2c | -12.48591 | -53.83865 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdcfdd30-4fe1-3c5a-9c29-353ec6e5e981 | -12.95057 | -48.06374 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 163c6eaa-b8ea-32a5-a361-95103746f55a | -11.0936 | -45.12293 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34156b72-3bb9-34e9-a1e3-f65aa50b37c7 | -12.91619 | -56.93874 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92dcaac4-03e1-35d9-879d-0a37bd4de6e9 | -14.56567 | -48.04181 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 589516df-bfe9-349a-84dd-a643773aebba | -13.50767 | -46.92026 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8e9ace5-76e1-3896-80f7-417c091bd8d0 | -8.08866 | -47.58761 | 2025-09-04 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59088b8c-5da3-3a3a-9c6b-65c87712bcda | -12.48868 | -48.07815 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f934cf42-f874-3c80-8b5e-988e62e2fa21 | -15.00433 | -50.05575 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01730192-f6fd-3afc-bdfe-abc8d9b8a7ce | -12.89237 | -56.95107 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a20613d6-e6ca-354f-a186-458c1bf7e0de | -10.94959 | -51.00185 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e15868f-31db-3161-bbba-d9c81050474f | -11.5916 | -52.16478 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a4ef6ef-b896-3edd-9fe2-5c1be1f2d02b | -11.95579 | -51.34269 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 042180f2-581d-30eb-93ad-dd815009526a | -10.31282 | -46.36813 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1c9d6d8-7326-3294-952a-dc742893121c | -9.30016 | -47.08934 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34f19978-0205-303c-8be9-f4b6b378d4b3 | -9.43428 | -46.77212 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a82028a-09ed-39e1-8fd1-c3f18e4b43a2 | -11.09495 | -52.02518 | 2025-09-04 04:27:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0fcbd37-8e28-3f6c-959f-30f7229335dc | -10.98271 | -46.85321 | 2025-09-04 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19e6f334-3b73-3cf7-90ec-77479e181ee3 | -10.57915 | -55.41098 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f5c240-a8ca-3a03-a0cb-a43db8151f83 | -14.81163 | -48.34056 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e9638b8-63b2-3b9d-acaa-461c78fe6c9b | -14.54089 | -48.07042 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c62c824e-2210-3eda-939c-d7a741967405 | -12.46555 | -48.07436 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0742b748-882f-3c46-bce4-89912059b1cb | -12.49309 | -48.07166 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e1809da-a0fc-3e8f-978e-f5fa131739c6 | -14.75529 | -48.09126 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72f972d6-a7e2-34fa-b6e1-ee7d116efd9e | -11.2345 | -44.9626 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c838dd3-b719-3329-a5f0-7705d166ddf5 | -14.90663 | -49.6252 | 2025-09-04 04:27:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcb4c21f-9976-3ae9-bd37-cf7f826bb113 | -9.61892 | -40.61066 | 2025-09-04 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd115606-e5c6-3bce-aebb-5dd754236056 | -11.58772 | -52.16412 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1de87af1-d22f-31c3-b8f9-3085d351285a | -7.71047 | -50.24706 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4996c2c3-5531-3fbc-8ea7-79123f3c1414 | -13.9954 | -49.55855 | 2025-09-04 04:27:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccc83a58-9e50-36ae-a232-76d417ecb528 | -14.1988 | -48.0834 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91cb5e48-fd7f-3efc-87bd-8d10f61043e0 | -11.59329 | -52.15485 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76ace004-4dec-359e-8b2b-2164f9f0eb28 | -14.7826 | -48.13566 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5641230e-dd08-379f-bc55-834332157797 | -14.39099 | -53.07614 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2702b40-e547-3183-a693-85b61508e13b | -12.17963 | -53.88947 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 920f14ac-d55a-3991-ad74-3b05c5b00583 | -7.74333 | -48.76413 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 03b59504-1dc3-3fb6-9ed4-d75a7daa662f | -14.97547 | -50.19017 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9011aa8d-8a46-33b2-b307-24e1961a1a93 | -6.74648 | -58.73254 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 37cc472c-8697-321a-b947-688a6555ecc6 | -10.11952 | -46.23234 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8db42f4-a244-31c2-ae47-ff6e50ea9184 | -8.57632 | -50.23505 | 2025-09-04 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 760fafe6-0d04-31a5-836e-d2ae6a997117 | -9.6186 | -47.03339 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d97a022-3d17-3549-8ab2-edc5e7b1231f | -13.73444 | -46.92634 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d028b4ef-5ac1-357b-921a-49f2b9e429b2 | -12.4716 | -48.07896 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7318923a-7c87-3120-a4e6-ae28f93b97ac | -8.35243 | -48.32229 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2c84de2-e579-3db9-9398-a5871d6ac193 | -7.96837 | -55.29476 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc0bb5f1-fdb6-32c1-84ac-93df7c58a1ba | -13.85578 | -47.97281 | 2025-09-04 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c2e2cb-8a12-30eb-94c9-18b612be997a | -14.21973 | -48.07957 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c825412a-88f4-39ce-b7bd-1f9dd3461cfe | -6.74553 | -58.7378 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 064e673f-3871-3085-95a9-07f39934e957 | -11.0252 | -51.51284 | 2025-09-04 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae02e66-0507-37db-b935-c5da3e5946ed | -8.37821 | -48.3338 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7d33f71-beb3-3613-9eb5-721c09341ced | -12.48943 | -53.84352 | 2025-09-04 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29fa271a-ee05-3cde-85bc-1c825092e31d | -11.58618 | -47.76165 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d9df78a-d53f-37e2-9c05-5148888a9282 | -7.96765 | -46.34065 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README45.md)
