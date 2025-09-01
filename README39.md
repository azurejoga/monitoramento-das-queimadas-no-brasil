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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2813a36d-8330-357b-8c2f-ce4b33be8e82 | -7.08203 | -44.3441 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61be688d-332d-3fc4-bb15-d560030e7c8f | -6.29693 | -43.55351 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41e2da79-08ab-3fb0-823e-2256bba9559c | -5.90809 | -43.34579 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e841f12-f745-32d4-bd22-3709fabd2140 | -4.5524 | -46.43837 | 2025-09-01 04:10:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a86520-1f19-3f97-8ab6-85e9c8f1837b | -6.94511 | -44.3394 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd162ac7-c4c3-306b-8edb-495a413d7a89 | -4.79542 | -48.11977 | 2025-09-01 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e83fd6-5b9d-3046-9ec9-a8870c0a5afa | -7.95071 | -46.35701 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ea83bf7-93ce-3158-8695-138ae6f80048 | -8.4431 | -47.36048 | 2025-09-01 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b392f53-7c1d-398b-8b94-0923f19ffa9e | -6.41104 | -43.62613 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d32fee3-f059-37ac-8db5-608d0f71ca2f | -8.84629 | -47.50626 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61bcc5b1-9939-38e0-b049-18d7ac1ab0e2 | -8.82351 | -47.83586 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bc9eeac-d77b-3af4-8382-19c612e38bdc | -7.06977 | -44.32963 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 668fb2e2-92ae-3602-8ea7-5562550c1fa1 | -11.8131 | -46.4144 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fda3a97-6483-3eb8-b708-c3fe16e12de8 | -8.82681 | -47.48772 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9ceeb86-673a-3564-926f-ec278887367f | -6.18665 | -43.34644 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c17bb9e2-321a-3202-80ae-08f0b93d2ab9 | -6.15817 | -43.33488 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d45d2d1-6296-346e-b5d3-1cea5aa58aac | -11.34125 | -43.51608 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29240c6c-1ac4-3fa9-b42e-549f620e5685 | -7.88627 | -46.99838 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb8dcec5-339f-345c-b6f4-00ade356b4d4 | -6.29752 | -43.61596 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8768f153-a8a0-3c2d-9b5d-95ca468a88d1 | -11.02815 | -47.06961 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a655d58c-9ed9-3fc6-bb2b-fa22339b9f8c | -5.76169 | -53.40424 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11d97377-8bdf-3cbf-adbd-06f1cc1d1c58 | -9.02569 | -50.11758 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d3dfdba-8b2a-3917-be4c-8d2e204c1ded | -6.36893 | -43.55675 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cceb6706-5e27-3a22-85b8-5af4739862e7 | -11.65275 | -44.86146 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af00322d-ddca-3010-9174-8dbff3ec2d6b | -10.23741 | -51.1134 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d9f5d6e-19e9-317b-9bd5-2b8d7ceaf2cf | -11.79511 | -46.42993 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 903e968e-13a5-323c-b6da-2ddb5fa790ba | -5.73287 | -45.53507 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7ca3dae-29fc-3a04-864f-f97cfe6a7282 | -10.24076 | -51.12403 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1f6b35f-d6cd-3931-a21d-1b161b26c756 | -7.45991 | -44.82225 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfd8c52c-31fa-3c3b-a9cf-7780b05aad9d | -6.63846 | -43.96252 | 2025-09-01 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93b2eed9-3a4d-3f94-a02a-a0ddae508526 | -6.50963 | -43.5555 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d887177b-257d-30a2-828a-94b6205cdca7 | -6.15026 | -44.14211 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3437bebe-7049-3736-b3a3-1a9ce6715806 | -8.49681 | -44.73765 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 784d31cc-86d1-3191-b439-3ed7a5e2d153 | -5.44253 | -42.82873 | 2025-09-01 04:10:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e676736-00d6-33c8-b3ff-f050a386a25e | -11.35607 | -43.65858 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 412d4b15-34b6-3670-83a3-4ffb0bc61014 | -8.81925 | -47.83513 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d284b066-849a-33b4-b762-9b921897d002 | -5.8846 | -44.319 | 2025-09-01 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e0774b8-be89-3dd2-adc3-6f44eb0fdaf6 | -6.44265 | -43.96788 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2b07ab88-602f-3aa2-97fb-7e6ecca92f1d | -11.00978 | -46.85216 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dbed2bb-c9eb-371b-a013-0111da0049db | -9.38925 | -48.00919 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b010b08b-4ffe-3b42-ad36-186dff58b74f | -6.15713 | -43.31935 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 223f7f62-afbb-38a3-a8c1-eafcddb7f35d | -12.14532 | -44.96598 | 2025-09-01 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c8e2d68-69a2-3664-912f-d13c1731dff5 | -8.82421 | -47.83184 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4089d57b-cfb5-365d-a9e3-c003af4a32f7 | -7.25024 | -44.23864 | 2025-09-01 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d0c8245-2c89-3c81-812f-0c07ba9ff508 | -11.38089 | -43.63311 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61059ce9-7625-386c-b389-a27a127b23d5 | -8.20009 | -46.76842 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f701dc1-2c64-3aa0-b434-2eb02389f984 | -6.19131 | -43.33955 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca66f1ec-fdbe-37ef-a266-7064323d53f6 | -7.41497 | -47.43058 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd8ba2fa-2d73-3c7b-b5ae-16ff7052a2a1 | -7.07362 | -44.35095 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16d73ed7-41c5-3b2e-aa39-2161fb0d50b2 | -10.75102 | -46.3611 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9e72bec-e169-3149-95ef-3d9b22cb6294 | -11.01816 | -47.0574 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aafd8ece-05b1-3015-9bc4-edbc1985d237 | -11.02902 | -47.06459 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edfe82db-310c-3b80-8eb5-62ec4e7ab354 | -11.48663 | -46.80669 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c707e89-4921-309d-93f2-4ff0a1ce1e28 | -6.7471 | -43.78452 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 119fb95d-8909-3a37-abd0-7bcc007b2478 | -9.26179 | -47.12824 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7b2b4f6-557f-3439-b21e-5a04913185a2 | -5.85338 | -42.53051 | 2025-09-01 04:10:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a565708d-194d-34ba-81d5-e999c6ee82ea | -6.52368 | -42.94719 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa55fdce-605e-396c-8a8e-a7f5e28806ad | -5.73207 | -45.53988 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e894be8b-551b-3be8-941d-80a6dc7bf906 | -6.19989 | -45.37586 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59da2c78-dc4c-3b7f-ad55-d37a1e834826 | -6.82485 | -52.81953 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f7e8b38-a3d9-32eb-92f8-1bc9729781da | -6.80131 | -52.80978 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c9473f7-1751-32cd-b44a-8bc1239ab381 | -7.66292 | -49.84971 | 2025-09-01 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9857e5eb-2ea3-3203-b39c-8185cb5cb48d | -11.81765 | -46.41015 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb0b6613-e89e-3c94-b841-042161ed2d58 | -7.08688 | -44.33669 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2f7e623d-faa8-3cd0-86d3-6b7415b93a08 | -6.18807 | -43.31604 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d689843-2563-338e-a643-9c3dd86293d4 | -11.01456 | -46.8476 | 2025-09-01 04:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb4c642e-b114-3a5e-a0cd-2e1e3d52a8e8 | -6.51839 | -43.54525 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d2962e1-214e-3296-aaff-f8808d4a829d | -11.0538 | -46.92031 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0952e992-efad-316d-8bfe-cc10fab57b31 | -8.06046 | -48.41491 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 856fc377-2098-3c50-84d9-1bcab4a8e89d | -6.12648 | -42.9437 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e8709a0-8a70-37ef-9206-a6bfc6734046 | -7.06067 | -46.24366 | 2025-09-01 04:10:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cdfbf2eb-2514-34dd-a9a6-0cd58f0340ab | -6.80528 | -45.68659 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b96b35d5-6af9-363b-91fb-9d4da71b4c83 | -7.4002 | -47.44048 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 189552e3-a0d8-35ba-9b85-2efc59e197c7 | -11.05297 | -46.9252 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c10fc39f-8ff1-3452-aeb8-0a68634306d9 | -5.35098 | -45.78167 | 2025-09-01 04:10:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27d8a761-9d0b-3a48-a003-e60430990072 | -9.66502 | -47.05546 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14801393-1713-3ae4-9271-f2c27c0c8a7c | -7.63281 | -46.55428 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1258f4d7-ff8e-38ec-b135-777b924ba9d5 | -11.02294 | -47.05306 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ad67907-574d-30cf-bef8-418f05832755 | -11.02715 | -46.98215 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 312cc7c4-03f3-34b3-a5cf-121682c68077 | -8.84427 | -47.5178 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 354fba13-027f-3f8f-ba2c-05a7be3b5a5c | -7.08848 | -44.34938 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 984e2c75-149e-3c19-8056-1533a972e876 | -7.10597 | -45.34211 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a16d06b2-0339-3f3e-92ab-5f088fdc52c3 | -6.16783 | -43.33192 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d4ba5d6-5b94-37e1-8420-937161170623 | -8.84213 | -47.50553 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b75bba47-4b65-384d-8973-a8c90fa79bd1 | -6.29923 | -43.29951 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc42c447-69db-3e70-b6e2-8b4abc6e064d | -6.30651 | -43.64862 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 43839f9e-c2ea-3004-b3b0-48f19029232b | -11.05245 | -46.90495 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f58ebfc7-7750-374c-9bb5-c588483765cb | -6.1901 | -43.34699 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6bd12d5-3937-32c4-b812-b91f44dad3f6 | -6.94881 | -44.05016 | 2025-09-01 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05517322-bae2-3dd5-8f63-4cff8a9d483e | -9.67423 | -47.81845 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d9c5146-5440-3ac8-b03c-1f8a7f140534 | -11.04752 | -46.98026 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8243a96-5650-351f-a2ae-bcb638b8584d | -11.91355 | -44.88421 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5a0030d-764b-3e0c-805b-3ed1ac98fac3 | -12.31008 | -45.68456 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33244d2d-1eb3-3ecb-8dfb-8f3a67adaf8a | -10.23655 | -51.1163 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e0b95b0-7e14-3e4e-96f3-da963e4ae186 | -5.99751 | -43.35168 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76b0c44f-cfbe-32cd-a3b6-d7dd520347cc | -6.25878 | -43.38122 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e28703a0-8cc2-384f-8a52-2cad6b3c47aa | -6.54501 | -44.57557 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 331ce8aa-1baa-3f62-b94f-f8578fc1fb96 | -11.36991 | -43.59436 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73c0221d-4d54-3201-aab3-6c471e393102 | -5.74855 | -43.68523 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4902ee6-67f4-3662-9f84-03a85e5c7bd6 | -8.15911 | -42.30465 | 2025-09-01 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
