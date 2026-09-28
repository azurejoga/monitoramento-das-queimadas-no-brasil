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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a4fdd50-073a-3215-9f11-55f7b6d4fc00 | -12.04981 | -46.49482 | 2026-09-28 17:07:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c3c87cd6-9397-3e57-add3-88dd287cb9d0 | -15.18736 | -46.14526 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f0e1b585-8dcd-37ff-83c3-1ca64c9952ef | -15.11179 | -53.90503 | 2026-09-28 17:07:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5f56571f-b713-301b-a95a-6ac435b53b80 | -14.08988 | -44.28665 | 2026-09-28 17:07:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a6b29c17-5782-3506-acae-0f7f7d8a3acb | -17.04062 | -56.57534 | 2026-09-28 17:07:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 754111c1-4b21-321f-a6c2-a70dc0d1dc2d | -15.1538 | -43.59424 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| d7839af0-36b8-3ce1-a472-8ffe947f0dee | -15.06234 | -54.59743 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 9e2ed6c4-3899-3f97-b407-d992ed5148a3 | -11.89721 | -47.02536 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| d51a8032-1f80-3f66-9361-2c37fb9197e2 | -15.93381 | -56.25893 | 2026-09-28 17:07:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| d274dd64-6ae9-3260-95a7-d947a12384fb | -14.10519 | -54.03249 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 07b46e0c-bd81-339d-a2cf-ea580272b6d7 | -12.62748 | -47.27256 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 83adbcb2-4e3f-3c8f-be10-10e1720f6362 | -15.75707 | -42.28024 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ae446575-b7c8-3aca-9978-73dab3294d9d | -13.40332 | -51.31988 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f88e3289-58f1-302c-9dd4-30cfc3f25aed | -14.32653 | -44.80357 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ad29c7f-7897-3692-b82e-a940e5997287 | -18.74328 | -48.13139 | 2026-09-28 17:07:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| cfb28be1-fab0-39ac-9945-7cbf916a9d4b | -24.84908 | -51.33136 | 2026-09-28 17:07:00 | NOAA-21 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c882822f-8045-34f2-a625-126e7c4a597a | -13.36611 | -40.97478 | 2026-09-28 17:07:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| a602a9b9-92d4-3d19-b59a-cc9e957b94ae | -24.82415 | -51.05545 | 2026-09-28 17:07:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 30810e19-acbc-39cb-a29b-5bdcd32f69dd | -16.42041 | -43.29054 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 20d2f8de-949e-3b9e-b03c-558bd70b4b0b | -14.48566 | -43.70855 | 2026-09-28 17:07:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 257af197-703f-369d-9b23-7e5a9bea42e3 | -12.68746 | -46.97971 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5a5be1b6-d9a7-3244-aced-1c5de2252936 | -16.43673 | -43.49278 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dab55304-e4d7-3ec2-8534-bb4d76688bfd | -15.93323 | -56.25476 | 2026-09-28 17:07:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a6c4108d-53d7-3a56-99ad-42b2f4c77cf1 | -15.04735 | -48.5704 | 2026-09-28 17:07:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 207e0480-1be8-39e8-8d56-718179cbe87c | -14.15785 | -40.73521 | 2026-09-28 17:07:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 4ef4615c-50e2-34f1-be1a-960b7f8af0d8 | -14.72359 | -41.59273 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 156.0 |
| b41ba289-0386-3af2-8399-b48528a2b3a8 | -11.68296 | -44.52142 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 18cb0f62-b559-3390-82ae-97a0d82ec8e9 | -17.53545 | -43.68441 | 2026-09-28 17:07:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d910acc0-e036-3b0b-b5df-3b235a7f4c2d | -13.90793 | -53.67227 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a5d00080-904b-3241-bc51-ca861d566d99 | -11.9016 | -47.00154 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| addc0e45-93fe-3048-8668-0a08f7043e4a | -14.08064 | -46.32906 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3b06053a-004f-34c2-9f3a-7f674612335a | -14.7534 | -45.64962 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 737faee2-3da7-3484-a5c8-8f0abebbcf51 | -15.16197 | -43.60032 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.8 |
| eb2c47dc-e77e-382c-818f-86a9d4b689ac | -17.81491 | -44.42614 | 2026-09-28 17:07:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 689001d8-a01c-33d1-b7bf-7da528666ad3 | -13.70803 | -48.82338 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 68f408ec-aebc-3ae3-8357-85b2814af22c | -15.03897 | -49.59895 | 2026-09-28 17:07:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 0bb06224-b053-3eb0-aa46-70779e4930cd | -15.17538 | -46.13223 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 875adc49-cea6-3d1d-94ac-e95b8d6ebcfa | -16.34948 | -42.57124 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a6e48c4b-2f98-3c11-bd4d-894c1180d6cc | -16.34717 | -42.57076 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 4a790507-00bf-3bd4-89c9-a29fbd84f5ed | -17.59606 | -45.80489 | 2026-09-28 17:07:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c4600ca-b4b2-3fd9-a18a-d6e63c37403a | -14.08721 | -46.31283 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b1e56193-d110-318d-a639-9df8a5828b34 | -16.20336 | -47.85757 | 2026-09-28 17:07:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5530cb7d-fe6d-3af5-aec9-564173ad0798 | -16.15235 | -42.85067 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 29385ae5-9d2d-3318-bf29-812cafa08cbc | -11.67917 | -43.51287 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 3dea84d9-c098-3120-8d81-d9bf3aa0475b | -13.46674 | -48.5913 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 32843157-cb19-321d-8dbe-1de79857fc9e | -13.97333 | -54.01337 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2d92ed71-ae8e-305a-92a3-90ed7106fc3c | -15.1484 | -44.03536 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a0d67359-8927-333b-b3cc-4e4d167733da | -12.74932 | -47.29366 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 92f6c805-ea2e-3556-ba6a-a0f306a4b6b9 | -12.87909 | -44.79023 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a0c5eda2-9afb-3de5-a8dc-fc12594b6b05 | -18.67815 | -48.61952 | 2026-09-28 17:07:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4e486870-4b45-3657-a6fb-d21387d56d14 | -18.92917 | -47.20221 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9fc58409-9d7f-343f-9a36-bdede929ffd8 | -11.26332 | -43.53648 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| df5dafc5-6c99-3548-ab6c-71d0d4651a75 | -11.48816 | -41.76405 | 2026-09-28 17:07:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 82a4e345-cc50-3a1c-ab74-ccf1ff46fdd3 | -17.20302 | -46.63306 | 2026-09-28 17:07:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e1f1c54b-60c5-331b-a7e1-bd68611aeb02 | -15.5881 | -47.91091 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7cba7ec8-7daf-3d9b-8b8f-a890b7076926 | -12.06476 | -45.74266 | 2026-09-28 17:07:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 2eb00157-c076-3efa-a8c3-f7ec83179476 | -12.75376 | -47.29275 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d8a42f74-153a-39e6-b724-acb745a5ec81 | -15.18941 | -48.43261 | 2026-09-28 17:07:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 039ce321-b654-369a-ae84-550ea5229945 | -14.30889 | -43.73647 | 2026-09-28 17:07:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| bb71b1b0-45d1-39fe-bbc7-b33c7a48caea | -17.67279 | -42.01239 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.8 |
| d9bd88f6-6629-3ba6-9604-9a1a7f5247ec | -15.04052 | -48.03786 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b24af651-9a2b-35a0-8c58-f3cb9679dde6 | -15.1515 | -44.0303 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 246dd078-cde7-38e7-9415-2706fea15049 | -13.55102 | -43.48788 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b82bcdd7-ef17-3721-86f3-3269c1c92507 | -15.41193 | -47.93211 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ee0b654-c245-3bcc-ab9a-1921b2e23b67 | -14.48666 | -53.63547 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e32c7cff-a36a-314c-b406-640ce7a48b1f | -13.98048 | -54.01586 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6a270593-f721-3dee-b58e-7ce9d1d57ac3 | -11.26509 | -43.54007 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 0b2142ff-5afd-398d-8a98-7b8e1bbe04c2 | -11.89595 | -47.02261 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 26ace93b-46f1-3fca-8813-beca1a5a875e | -12.97378 | -51.08803 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.4 |
| bc61c027-12d9-3ff8-b92f-adcf32134e96 | -14.71738 | -41.86848 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 8e9ca3d9-0fef-38e7-a43d-85a8e356f8bf | -12.75346 | -50.68451 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| d4eceb71-9910-34ca-a296-985f0bdc1c71 | -14.5834 | -41.23852 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a7e1c93e-c85d-3ed7-9dda-923d0682eeaa | -16.34901 | -46.87508 | 2026-09-28 17:07:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c63f27a9-9da6-3d97-a6bf-8d6dc1093927 | -14.19891 | -44.93938 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 24d19224-4915-3ac9-b7b7-4f762485e1b5 | -11.9838 | -41.98555 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| adbee06b-4d6d-3f68-92a1-28ec2d02da87 | -15.47414 | -46.13517 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bfecc30e-31ce-36cc-a1ae-da007e6ee42a | -12.90344 | -52.06062 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 10d5d6f0-5355-372a-b852-77a4805ee680 | -11.32384 | -42.21523 | 2026-09-28 17:07:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 4fc39434-8a3d-3601-955d-efb8a9e2b13e | -15.49531 | -41.45076 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 5a364c34-2a2b-3bec-9ec6-fa8614623be1 | -15.21549 | -46.19423 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fb089a77-b3a8-37e5-bf4f-ce7ac99ab7f0 | -20.83623 | -57.69222 | 2026-09-28 17:07:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| eef476b5-05de-3a16-a283-0c5b642b95e1 | -17.56218 | -42.52766 | 2026-09-28 17:07:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7321918-ef94-3064-8d42-943ef8cb2044 | -13.16779 | -48.55843 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4a30dc0f-1079-3839-b0ac-7b3de7357e19 | -14.20339 | -44.93525 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a66ba722-9a6b-3692-b178-ebdf35140aa8 | -11.90181 | -47.02448 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e2894661-ee4c-38bb-9936-31c8d1c7434b | -17.57341 | -44.39305 | 2026-09-28 17:07:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e15011b2-b32a-3181-9f71-819187d1b88a | -15.07011 | -54.6037 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 80fac17b-3b8d-37cb-af06-fb092b3377d9 | -12.70298 | -47.33361 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 03640c9c-508f-31a6-903c-ac715e6323c4 | -14.5257 | -48.29865 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 39158150-7218-3fcc-8acb-166629350be5 | -12.62124 | -42.75404 | 2026-09-28 17:07:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 20891f11-4d5c-3187-a6de-800c1d354970 | -14.38106 | -52.10116 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 9ca3e4b0-da03-302c-a523-8f8dc841f436 | -13.67766 | -41.01439 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 612636a4-6184-3811-8f6d-f303b48162e0 | -12.18043 | -40.73399 | 2026-09-28 17:07:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 52db2a91-656e-3d3f-866b-221f39902c70 | -11.37554 | -43.43374 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 728b799e-c78e-3a72-86f5-e06ed4b60722 | -12.75419 | -50.68882 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 10d77abf-a1e4-3707-992f-d39d0aa68e6a | -11.70402 | -43.48576 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| efd0a706-28d3-3fe3-ac5c-d78b5cf52a3c | -14.50847 | -48.32132 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f2c45192-ada9-3e70-b365-97a4ce0ce968 | -16.50702 | -42.96228 | 2026-09-28 17:07:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a2147452-a7f0-3a6a-8c53-c0cc23b8bd79 | -15.07345 | -54.60319 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a80b325c-4e44-3d38-bc39-82787066718d | -18.33225 | -41.78597 | 2026-09-28 17:07:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |


[Clique aqui para ver as próximas entradas](README139.md)
