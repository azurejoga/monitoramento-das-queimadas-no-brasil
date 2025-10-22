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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ebbb507-fb08-3823-8bd8-14d73bd824fd | -12.50109 | -48.57124 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5ad822e-76bd-30d5-989e-858c4977c4e1 | -17.1571 | -46.12169 | 2025-10-22 04:27:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53a05e51-750a-33e2-b71d-04281df81345 | -11.80357 | -47.88593 | 2025-10-22 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d190d53e-59de-3e3a-91e3-1517847c37dc | -16.23955 | -52.90521 | 2025-10-22 04:27:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd55e004-3df8-3990-95a2-11a2ee8d4d13 | -11.95185 | -48.0653 | 2025-10-22 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bb35d57-0a41-378b-ac8f-0edf9d151aff | -17.38166 | -52.01213 | 2025-10-22 04:27:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e276d1f8-0113-3b58-a486-3439e729d3c5 | -15.53155 | -50.38497 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0165023-b392-346f-b9c7-d3d15b9db7e3 | -14.74819 | -54.11391 | 2025-10-22 04:27:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ff6d2c4-8bb2-3728-8f9b-7c7eb344ad08 | -15.49151 | -50.45749 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc87567f-03b9-3090-9113-d56e50bea70a | -16.87173 | -49.99532 | 2025-10-22 04:27:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c73e093d-844f-36aa-8239-52b9fe150b5a | -15.80992 | -49.86546 | 2025-10-22 04:27:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eb18427-e0a8-3246-8b03-cb7731f2028d | -11.08173 | -49.62572 | 2025-10-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 459f5d9e-2df4-372d-b232-7d0f3614c28e | -13.61801 | -47.04621 | 2025-10-22 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff801673-a34e-36b0-988d-366884c09273 | -18.30392 | -46.5948 | 2025-10-22 04:27:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 49a431c2-d372-304e-88f7-55251a8a9a9e | -12.69487 | -48.63654 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51254dd4-c3ca-37ed-8524-de0ee9f5ba79 | -13.4612 | -48.82674 | 2025-10-22 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db2a090f-d875-3038-9da0-7e6a183e0cbb | -13.84388 | -49.3194 | 2025-10-22 04:27:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c6ae426-645b-31f1-b3e5-1c1226d71765 | -17.64107 | -46.75191 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64cd11ef-0e60-3b5b-a580-46cbcc142242 | -12.51051 | -48.57643 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d56cfe5-26c1-33c9-a724-2fadb3574294 | -13.59172 | -48.43493 | 2025-10-22 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27c2aed5-c5a3-3157-8572-f200fd77059b | -13.46453 | -48.8273 | 2025-10-22 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0ea46e3-380f-3d42-a789-6d0f24d4970f | -15.48809 | -50.45684 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8a57766-5c45-33a3-91b6-f6e6ac5e2739 | -14.69365 | -48.78307 | 2025-10-22 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4176460c-2bde-3c5e-a79d-e3ba0f9012c8 | -12.83 | -48.75088 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10df3302-a64e-33ba-a12a-f5518984928a | -18.22014 | -46.06164 | 2025-10-22 04:27:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 573ce9d5-e0f4-304d-a187-a0e41509cdeb | -12.75382 | -48.60957 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ed1c61f-c82a-3d15-ab4b-2dbc9c5eee77 | -15.45204 | -48.2051 | 2025-10-22 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e9d72fd7-6fc8-34a2-b54f-dd2af6aca388 | -12.88979 | -48.58823 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2241323e-7ac2-36a8-a96a-e5dbd6f9c681 | -11.08237 | -49.62185 | 2025-10-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b6b806d-5e00-3a38-b69b-0058e7b131b3 | -16.0427 | -54.26519 | 2025-10-22 04:27:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 559c574a-741e-3919-971c-fc373e9f91e3 | -11.05534 | -45.39832 | 2025-10-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cf108be-5e90-3e76-a9cc-4a29be34dbc9 | -13.27137 | -47.00171 | 2025-10-22 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a0d04a-00b5-337f-923a-7b9d33f00222 | -13.00086 | -48.80923 | 2025-10-22 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbb2378f-8587-32d9-8418-71caaad0e9c3 | -16.82726 | -47.6392 | 2025-10-22 04:27:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9d9aded-5f43-343d-8003-160a97f7ab2b | -15.86983 | -48.81266 | 2025-10-22 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d502216-1261-3284-8e4f-cdffbfb08c06 | -16.3938 | -53.82273 | 2025-10-22 04:27:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e35219b2-ee31-3b59-9ce5-16d5f6e296d5 | -18.57533 | -44.92456 | 2025-10-22 04:27:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05100309-d632-316d-8245-29c22e69f233 | -14.5374 | -53.76381 | 2025-10-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99785673-dde9-3943-9d30-f11d5186103c | -19.30604 | -45.80511 | 2025-10-22 04:29:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8593c2d-3992-347e-8b1a-a161a46e5773 | -19.30968 | -52.7644 | 2025-10-22 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73876b56-e8e1-3ba1-9497-fd33182801ba | -17.40952 | -55.08239 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fe71fde8-3f5e-369e-98f9-88a4dedb0be8 | -17.41381 | -55.08327 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a00d3b24-3c82-3dcb-89fc-823f665af5ae | -18.94835 | -55.07375 | 2025-10-22 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| f8db74b4-42e6-3250-9dd7-c9599cd18da6 | -18.67206 | -47.05314 | 2025-10-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baee9454-f9b4-3472-9e02-efd9616d20c2 | -18.59537 | -51.72436 | 2025-10-22 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97e7d5cf-b411-3ac2-9074-0838f2e83e89 | -19.1574 | -49.1321 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87b01420-99d7-33ff-814d-5e1c0c40ab1a | -20.97944 | -47.21355 | 2025-10-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8327afb5-a7b4-3d91-9c0f-1f85d11445ee | -18.65094 | -49.08618 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8a4df9b-2415-311a-af56-86449babdbbe | -20.30128 | -46.5431 | 2025-10-22 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b2f8c7b-dcb1-3694-8549-8083138a198d | -18.65037 | -49.0898 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f36c07c8-1021-3c7e-aaa0-b0e959535a8f | -17.67388 | -54.21358 | 2025-10-22 04:29:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ce983b-eb11-3780-9bd7-f4d17d2134a8 | -21.21722 | -45.06318 | 2025-10-22 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54b51699-09d8-35aa-9cfc-b6b9d7821300 | -19.48575 | -54.93008 | 2025-10-22 04:29:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a22012f-cfd6-3d77-a519-08f5b77ef4fb | -18.33987 | -49.50475 | 2025-10-22 04:29:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1ca8d675-a366-3784-8417-bd0efa496f91 | -19.87216 | -46.3314 | 2025-10-22 04:29:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e31164fa-f339-3b50-824b-b2bdbe34e9fb | -17.41183 | -55.08286 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bce79cf9-3d0b-3415-96f7-2aa439226958 | -21.31219 | -44.78446 | 2025-10-22 04:29:00 | NOAA-21 | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a4b8b4a-a587-3f07-ac14-afacfff2b140 | -18.67604 | -47.0498 | 2025-10-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 952e1815-7e93-3aff-bf43-1d5ce6fafe10 | -19.15854 | -49.12484 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e50712a1-6546-313d-9043-ae1810779c2a | -17.83818 | -50.81322 | 2025-10-22 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af3debb0-1831-3aa8-9cfe-a519cd76d9e8 | -17.42121 | -55.08034 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8b693f0c-5111-3bb5-a825-68a3398d5d46 | -21.26123 | -45.17856 | 2025-10-22 04:29:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7ec16e48-93bf-310e-9670-a52088ac74fd | -19.1541 | -49.13153 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48efe66d-7496-3ec8-9e1c-f19fb7a2f825 | -19.91218 | -46.12017 | 2025-10-22 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d07279d8-0b1a-3bbe-b64d-8918efe71337 | -17.41101 | -55.08711 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 859420b3-e2b3-37d5-9d1c-b6ed8f232309 | -20.56556 | -45.89669 | 2025-10-22 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e18b99ba-da12-3d8f-a8b1-a928ab117c31 | -19.1591 | -49.1212 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4fc129-deae-3498-993e-0e471f2a5329 | -19.14888 | -46.33939 | 2025-10-22 04:29:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 361b9906-1b42-3c0c-bf76-a3e124db1e50 | -21.89805 | -50.67086 | 2025-10-22 04:29:00 | NOAA-21 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 65b59dec-b0ad-3a33-986b-9c4ebf3fa559 | -21.26056 | -45.18367 | 2025-10-22 04:29:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e97f562-b59b-3b09-b80f-0f323cb06c63 | -18.11507 | -48.53106 | 2025-10-22 04:29:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb5bbfc3-96e9-32a7-9ff0-76992e37104a | -17.41265 | -55.07861 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| db70fac4-e1de-357e-9ca1-a04ec53e1c74 | -19.83589 | -46.54075 | 2025-10-22 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcc8d7b7-e521-3223-9bf8-51988274c237 | -19.91277 | -46.11587 | 2025-10-22 04:29:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dcb451b-09e5-358e-9a69-d3e900c45ebc | -17.42203 | -55.07611 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2d9df5fc-aa0f-3172-8f13-7462378ed044 | -24.11056 | -48.21468 | 2025-10-22 04:29:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 07158fc5-0e7a-36a2-bada-f4ed6c334eaf | -20.42066 | -55.7392 | 2025-10-22 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 68581c8b-246c-3381-a704-d0769d11a0fd | -18.01005 | -49.39546 | 2025-10-22 04:29:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d3d93c6-c252-3ff3-8a9a-66d9b3e323a0 | -19.16241 | -49.12177 | 2025-10-22 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0a2adbe-d615-323e-8a87-b25373c3fdb9 | -20.42147 | -55.73493 | 2025-10-22 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a78f28a7-9247-365b-b147-041b82bd8540 | -20.19081 | -47.04965 | 2025-10-22 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af2bdc04-21b0-3150-a90d-20bcf088cc42 | -18.6465 | -49.09285 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f9008d1-7600-3a67-8676-77074e8ecd47 | -19.81779 | -53.08518 | 2025-10-22 04:29:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbaed4e7-bc26-328f-a02a-cec6128e27b2 | -23.26194 | -51.03664 | 2025-10-22 04:29:00 | NOAA-21 | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 392d36d1-8311-39f1-8130-8e51f728d8c2 | -22.38231 | -46.91752 | 2025-10-22 04:29:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d57a5b8-7795-352a-aba4-0a75a35c5d35 | -17.40672 | -55.08625 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8ee702a6-c1c3-3f43-b245-8e689de4a831 | -19.09253 | -44.3403 | 2025-10-22 04:29:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0bb5556-dabc-3772-8f75-e3689a1374e6 | -18.64707 | -49.08923 | 2025-10-22 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe20e396-d451-3862-880c-a117baf31ff5 | -20.56252 | -45.89145 | 2025-10-22 04:29:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69253b02-67ac-3430-a8d7-981090e203c3 | -17.41032 | -55.07813 | 2025-10-22 04:29:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fbaad02e-a529-3510-abbb-3ed86d26eb2e | -20.98001 | -47.20957 | 2025-10-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49d6a221-acee-3277-b2eb-c6b9d0c6a60d | -20.42569 | -55.73587 | 2025-10-22 04:29:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be806fc8-a0a8-3984-9875-84205c5d0b01 | -20.13095 | -41.80135 | 2025-10-22 04:29:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 741af3b9-e255-3052-ab2d-44fc41d557ea | -20.02701 | -46.87576 | 2025-10-22 04:29:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34167235-1bd8-3a7d-8d8e-960f322a7946 | -21.05583 | -46.98606 | 2025-10-22 04:29:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0f06d66-0be3-331c-812f-9b962a2c7e6c | -22.12596 | -47.02479 | 2025-10-22 04:29:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ff8704b-5c15-3a02-9878-1e1a9725a897 | -19.26484 | -51.9765 | 2025-10-22 04:29:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0e89a6a-3532-3afc-be27-100ef7c86ee5 | -18.46165 | -48.46635 | 2025-10-22 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd0f2b4f-e2b4-3dc4-9105-e1a5df86b8b3 | -18.59257 | -51.71963 | 2025-10-22 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1471d9cc-3127-39ae-8010-b66ea8151122 | -18.60679 | -47.32731 | 2025-10-22 04:29:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
