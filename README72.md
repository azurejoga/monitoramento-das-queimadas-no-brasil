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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 213aef1d-9c7b-3452-82c7-9460cb2d0831 | -9.21007 | -59.61411 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5907714e-461d-3a4b-9b57-b8c2226db26a | -9.94888 | -60.17903 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf468a9-76a4-32cb-8b27-d8a38d98564f | -10.46978 | -59.13243 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 398f37da-b09d-3db6-8591-e9dbeaf71170 | -10.45923 | -59.13435 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da09dd20-4c48-360a-9e1d-d7d1934480ee | -9.15799 | -59.5986 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e123e87-f5d7-329c-bb9d-c060e7ffa135 | -13.42941 | -57.16721 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60e27af8-6772-36b8-a665-35c6441e7146 | -9.17518 | -59.70522 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39a23ca7-aea3-3982-8e5e-70199bf38e7a | -15.69917 | -48.08738 | 2025-08-23 05:21:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bf86a2c-71a1-344a-b6b5-2a150fd26464 | -8.9217 | -60.72179 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ee0f45-d2ff-3f81-83ec-969d6d5e5f1a | -13.36537 | -54.40488 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a662fc2f-e4a7-3e26-8db8-dddbe441c845 | -12.5879 | -60.35432 | 2025-08-23 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0775513-6cbe-32b6-a181-c0b417cd46e9 | -7.80251 | -63.55395 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72900203-d28f-3f5f-9fac-6990f5bbcb5d | -13.02364 | -56.83276 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 542f1746-9719-3805-8e57-83c13677c544 | -9.25046 | -59.61335 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec15da28-fe72-3622-a807-81a031cdf5eb | -9.17075 | -59.71169 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff42c6cb-86ad-3848-8e3a-2855ce728916 | -8.89235 | -62.4101 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14683014-b4fd-3d12-8057-a71693c28c69 | -13.36452 | -54.39817 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e8f967-bb41-33df-9156-38b5750ea3a4 | -9.50425 | -60.50674 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bf7aca71-3dd8-3152-84c7-897a018594f0 | -9.18902 | -59.6179 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 22c4dc15-a9c0-3d1c-812f-69c160b5c283 | -13.46819 | -47.03025 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e5d3b466-f840-32ca-9b2b-54d7e79bdbd8 | -15.01975 | -54.89096 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb850229-600c-3d8a-9397-6b49690d9c92 | -7.55492 | -63.86239 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06409688-c869-360b-8a07-6e8667f15900 | -8.44487 | -63.85935 | 2025-08-23 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f922b855-34a9-3989-a031-b49be26bf258 | -7.72921 | -67.06717 | 2025-08-23 05:21:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 853b5313-97bc-36fc-8aa2-d5b6415c043c | -11.19226 | -55.0361 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abe044ba-bb77-3233-bd2d-64b69c4b729e | -8.68997 | -62.86718 | 2025-08-23 05:21:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35f46ce8-e355-3531-95aa-c3301010044d | -11.50779 | -50.47034 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8231c91c-e8af-3626-9f63-049612f9c46a | -14.57833 | -54.50715 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 918a2f39-cd14-391d-8fb3-ffd207d68ca6 | -9.47863 | -60.32399 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebd85ae7-12b3-300b-81ca-7cee32c5946d | -14.47218 | -56.48449 | 2025-08-23 05:21:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c3b76f-90a7-3c31-b463-906542474115 | -9.19948 | -59.46556 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 296cff60-8a69-392a-86ef-268386bcb3a4 | -8.87747 | -62.43317 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f918d7a-ff74-3df1-a3e7-73c490522233 | -8.88244 | -62.4255 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 888521a0-d7bd-33e6-825e-93fadea618f1 | -9.24058 | -60.4789 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66d7c930-db75-3f10-a594-139d0430d050 | -14.61174 | -54.80122 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 230ed7ad-f321-3b28-a0c0-10e966f3ab10 | -15.07825 | -48.51266 | 2025-08-23 05:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ebdca97d-391e-389c-9924-a2deb1289919 | -9.16409 | -59.60315 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ae3c32c-8d50-3161-9372-d2804d988636 | -13.48154 | -46.89704 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4ef767f6-75d9-37f1-badd-c15950bfc111 | -9.52758 | -60.55448 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82ba3b26-7720-3a1d-b44d-e1da9065f16e | -7.4314 | -60.01252 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e3d7080-6b3e-303f-9a3a-d849208b3c77 | -9.18017 | -59.65228 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3169eb2-6d1a-3b17-bd6f-22c11db8182b | -17.87873 | -53.20356 | 2025-08-23 05:23:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb4ffbe9-ac0e-3d97-b6b4-5af58422af81 | -20.87823 | -55.00089 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de3427c1-5e94-394c-8378-767eb0b2ffc4 | -14.86054 | -59.61273 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 723b4367-cf52-3155-bd5d-345a59721d83 | -20.18851 | -50.9678 | 2025-08-23 05:23:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4cc157e-b291-3497-bbea-84006ed7b5d6 | -20.87419 | -54.99579 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fc6a012-200c-34f7-98a3-b4dffde3ff38 | -15.05167 | -56.39231 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1aa8dd49-ac78-3da1-b2fe-33a2be7c1a3e | -15.56597 | -55.00927 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86289d7d-847e-3c5d-b7ce-5777715437df | -15.61623 | -57.33163 | 2025-08-23 05:23:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bf021e6-225f-3dbe-8980-4f5bb3a8a43b | -14.63273 | -59.55338 | 2025-08-23 05:23:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65499312-2111-3ba7-871c-ae9ce9a51557 | -15.05875 | -56.39832 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cffd4ef1-31e8-3643-b95b-d916696bd3e1 | -14.86077 | -57.52314 | 2025-08-23 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a0119a8-c05b-3f7a-be9f-f35cb28cece6 | -20.8778 | -55.00261 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f273349f-99ae-3fed-b07c-d2ea4eb52042 | -17.26434 | -46.76578 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c6fb120-da48-370d-9f30-e74dfc067b83 | -15.06787 | -56.38951 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e08c4543-7412-394c-ae7c-c3c4ad51a2c5 | -22.21521 | -56.19272 | 2025-08-23 05:23:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e6bc919-0f1e-3344-ac84-de0481c27417 | -17.27172 | -46.76575 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 407d2e8b-e2f6-39da-b442-c6ad64146ca7 | -23.25939 | -49.50432 | 2025-08-23 05:23:00 | NPP-375D | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f60d53ab-2738-3bd6-a129-3129baea3d18 | -14.85661 | -59.61584 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3afd83f7-8047-3e67-8883-c8c9bca4b45b | -14.86783 | -59.61018 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 040f284a-86cc-30e5-8ee0-ff6bd0f43af5 | -14.81285 | -59.63145 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d39fe6b4-76be-3e48-827c-c705a66e9950 | -17.27274 | -46.76421 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c502c485-e2b5-3319-bf35-885310e5485d | -17.87813 | -53.20156 | 2025-08-23 05:23:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a88e676-73d9-3c63-8acd-47158a7932e5 | -14.76977 | -59.66552 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eebcff50-34e9-3288-bc30-29eae6f3ea37 | -18.96988 | -52.46985 | 2025-08-23 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 419ac257-29a9-32c5-af85-4cbd5275f63a | -25.56733 | -51.0588 | 2025-08-23 05:23:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e496df4b-06d3-3cc4-8d6d-0477f03663d7 | -15.54838 | -55.0112 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56789f06-879f-361d-8150-b4531da6c813 | -15.54361 | -55.01461 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 92430e60-be00-3aeb-b796-c0a3b91d1cab | -17.26535 | -46.7643 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cee01ac-3636-3382-86bf-a1a3614b331a | -15.06718 | -56.39449 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b66c60db-a460-3516-afbb-9e57043b22e9 | -15.65114 | -52.6819 | 2025-08-23 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6770d970-cc9f-3f22-bf88-42ebdd520f64 | -15.57026 | -55.00963 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ada77415-ea84-3ee4-8cfa-ed796922badc | -14.77032 | -59.66188 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13e1affe-4eda-3cec-8d3d-624eb360eea5 | -17.27209 | -46.77197 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11aa4d52-efda-30b3-a84a-ede2df8ca14f | -25.56696 | -51.06413 | 2025-08-23 05:23:00 | NPP-375D | INÁCIO MARTINS | PARANÁ | Brasil | 4110201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| aa388525-6d06-3b33-abc2-432d24e87354 | -14.85604 | -59.61955 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c3f1bc1-cbf3-30c8-b8a2-14f122283061 | -17.88308 | -53.20231 | 2025-08-23 05:23:00 | NPP-375D | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31562686-2330-396c-a134-5d99b6861efb | -15.54787 | -55.01516 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d5d470f4-46a8-38e9-aa6f-3e18eb5b6be7 | -14.86024 | -57.52545 | 2025-08-23 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a420cf7-edb2-3c1a-868a-d9b0a76d55bb | -17.26474 | -46.77166 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1a05016-5db5-3a8d-a1c9-e7dcd193e998 | -20.87362 | -55.0005 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 255b8234-a99c-3b6a-9127-ef294f1240de | -14.78319 | -59.6452 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac72cd93-b3d6-3488-acc3-61043b4ec386 | -15.02974 | -56.37909 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9f8d95d-dd95-3a6c-90be-3c70fa7e613c | -14.85997 | -59.61642 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a830b506-04a8-3fcd-a927-8b225b191105 | -15.54412 | -55.01063 | 2025-08-23 05:23:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82a586f5-3c29-3c30-8f73-99d84656650f | -20.87834 | -54.99783 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4497b908-1f11-3eee-b41f-e8911d115240 | -17.27103 | -46.77343 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de896319-5175-3580-984d-2dcfb2854cce | -15.06263 | -56.39887 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 204c3e40-4182-3113-a35b-608cb32c9741 | -14.81678 | -59.62833 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 087ffe47-e7e6-3449-9aa6-82c26519f1e9 | -14.86447 | -59.60961 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98511dc4-6f26-3fb5-9aea-4437db8781e9 | -15.03362 | -56.37963 | 2025-08-23 05:23:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7a7e1a8-db7c-3c9d-84a2-c284b6be3021 | -20.87372 | -54.99748 | 2025-08-23 05:23:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc82586-223c-3487-81ee-d970b8c0e6f7 | -16.51195 | -46.7337 | 2025-08-23 05:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e246a61-d933-398c-b624-3e0a22a5d3cf | -20.18893 | -50.96335 | 2025-08-23 05:23:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dac62433-02e5-3816-86ac-ecc9c0686354 | -14.86839 | -59.6065 | 2025-08-23 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5e3aa27-5344-3433-b147-211d62f96b5b | -18.97024 | -52.46643 | 2025-08-23 05:23:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 45e9857d-d97f-3813-8aa6-b6a6ae3add4d | -14.7748 | -59.65512 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16a197dd-78ee-345a-bda9-9ac859a66ac3 | -14.78712 | -59.64205 | 2025-08-23 05:23:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e16baf-aa65-3cc1-bd8c-a2c676feedff | -17.26369 | -46.77303 | 2025-08-23 05:23:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40d1018e-db8c-34f5-a997-5b5ae7169142 | -15.58647 | -54.2937 | 2025-08-23 05:23:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README73.md)
