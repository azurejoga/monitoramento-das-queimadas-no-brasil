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
| e2fc9510-97b8-398d-a5b2-42f905d852ed | -20.96494 | -48.77412 | 2026-01-07 04:16:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c912a956-2593-36a0-9f31-0af1f0f5e8da | -18.37084 | -39.95875 | 2026-01-07 04:16:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a4131a73-aa1c-3e3d-90c0-35dca1376aca | -20.22329 | -50.79582 | 2026-01-07 04:16:00 | NPP-375D | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 58249a96-a9d1-3be6-a335-cc11b0ea5786 | -15.54504 | -39.41343 | 2026-01-07 04:16:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11576afc-7aff-3367-bc5b-f8f3addf3a45 | -22.04202 | -56.30837 | 2026-01-07 04:18:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a7a7cc6-e59d-3633-b3ee-4e2825843c95 | -21.53886 | -57.53831 | 2026-01-07 04:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3eea80f1-8aa5-38d8-8ee7-8c0611887272 | -23.87035 | -49.74238 | 2026-01-07 04:18:00 | NPP-375D | WENCESLAU BRAZ | PARANÁ | Brasil | 4128500 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 88fb9099-d894-3cb7-998c-65e6b27787d1 | -22.03363 | -49.46817 | 2026-01-07 04:18:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c500b07e-05ab-3537-b16b-57ab8b0688d5 | -22.03739 | -49.46893 | 2026-01-07 04:18:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bab11471-a9a8-32d0-b122-d94b77571ef0 | -24.09746 | -50.13232 | 2026-01-07 04:18:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 97c1a77b-de1f-3e7e-9bab-1284a0d67626 | -21.53989 | -57.53394 | 2026-01-07 04:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f265f6a8-021b-3d0f-b9be-1d16e6ea0b13 | -22.49789 | -46.94315 | 2026-01-07 04:18:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a11ffc5-57fd-3abd-85b5-ab9f2be65353 | -20.53709 | -57.98923 | 2026-01-07 04:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 392cc100-b319-3be2-abec-bebdd67a9360 | -24.55674 | -51.96246 | 2026-01-07 04:18:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52fb8648-b7cd-3a33-8775-e3cf97b1c9c2 | -24.55342 | -51.95751 | 2026-01-07 04:18:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| af3dcc18-1432-3e20-9a93-060fdb573c35 | -27.01794 | -51.51102 | 2026-01-07 04:18:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eddfefed-2e42-3e08-b013-863a8fecf015 | -22.49854 | -46.93927 | 2026-01-07 04:18:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f60931f3-fec2-34b8-ab2b-ed417dca4fc8 | -22.73373 | -49.3539 | 2026-01-07 04:18:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ebafbe5-e60f-378e-8866-2a1b33faafaf | -27.42363 | -52.50365 | 2026-01-07 04:18:00 | NPP-375D | ITATIBA DO SUL | RIO GRANDE DO SUL | Brasil | 4310702 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d7f4f30c-3bed-3985-a528-9f4a10b3e9db | -24.09369 | -50.13152 | 2026-01-07 04:18:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d2d75dfa-6420-3b3e-a8d1-239f01eab7b1 | -29.88356 | -51.2157 | 2026-01-07 04:21:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 6b3db7b1-9b09-39b3-8ddc-96f0778b99a8 | -2.69104 | -48.99181 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13023c45-085f-3fa9-9f1c-3b95a81d3cd8 | -1.0007 | -47.55716 | 2026-01-07 04:31:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba0b1b81-9050-33ee-bb7b-ac3f1c056c22 | -2.87882 | -40.39857 | 2026-01-07 04:31:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6a566ecb-d2c2-3c4e-932c-5becef3e6bb9 | -2.16024 | -51.99257 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb6cdd2f-2ea9-36bd-8080-6fc4f648f1ec | -2.86157 | -52.80807 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d6bebe9-adc6-32db-85f9-e2b8f3edfc36 | -3.51768 | -49.72297 | 2026-01-07 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35504a74-2e76-3f18-810c-5c2c37244acb | -2.9569 | -54.0892 | 2026-01-07 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f26390c-5172-3e40-8557-1904b767472d | -4.5128 | -43.69459 | 2026-01-07 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72dd0baf-1cfd-3521-b40f-75d232a7ed3c | -1.71586 | -45.24457 | 2026-01-07 04:31:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3dd57b1-472e-34a8-a4be-bd0afed3cfe3 | -3.40027 | -51.87208 | 2026-01-07 04:31:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ebfd954-743f-39af-8ed7-3d341541625d | -1.71247 | -45.24405 | 2026-01-07 04:31:00 | NOAA-20 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89a04995-e7bf-3d1b-a158-b6b2f9223c85 | -3.00051 | -40.33916 | 2026-01-07 04:31:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c3f913d8-1b93-3f3e-9f0a-ae93eb0d7616 | -2.15845 | -51.97802 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82bb9057-dc41-3c41-b557-935259a5636f | -1.2954 | -53.90631 | 2026-01-07 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5edbfb2-38b0-3c8a-93a1-f7a00bdac4b0 | -1.66401 | -46.84206 | 2026-01-07 04:31:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af1328eb-b341-3ae2-997b-cc90c31cd42f | -1.31783 | -46.43125 | 2026-01-07 04:31:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e843e47c-e8fc-3dd7-bccd-ee4dba42fdfd | -3.54225 | -49.43508 | 2026-01-07 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3ebdf96-4cac-3d67-a68b-69db7abb0b83 | -1.8955 | -53.25497 | 2026-01-07 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86c954aa-8d42-31df-8ee1-dd1f5cc72080 | -2.74702 | -54.93767 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 25ad954c-44bc-386b-a236-8361c6a8be3b | -3.78886 | -43.36695 | 2026-01-07 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9e2e737-b5d1-3a4e-a67e-760111e56c6e | -2.08235 | -46.14989 | 2026-01-07 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38aa784a-1263-3ce6-8a42-953a8d06b3f1 | -2.75977 | -49.63919 | 2026-01-07 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4af6f59d-40ea-317c-9ea9-93469b8a29ff | -3.18503 | -48.62371 | 2026-01-07 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 921ac4c0-597b-38da-a55b-30282493ce28 | -2.43351 | -46.89595 | 2026-01-07 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8af33e6-5484-3526-bb6b-c9922af22e0b | -2.70186 | -48.98977 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbeb12cb-4e46-3fd1-acc3-f7aca61d0ae5 | -2.69786 | -48.99289 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f78a22-b47f-3247-b249-93b49a8995f7 | -2.87465 | -49.11482 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84d00c7b-130f-3203-ae5f-529933391215 | -2.90991 | -54.14576 | 2026-01-07 04:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee518af4-ab63-339a-bdba-6cbaa786f4f4 | -3.08264 | -49.48026 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81dbef59-67ac-39d2-a71e-13cc01e7e9e6 | -2.76265 | -49.64363 | 2026-01-07 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fabc35af-e494-38cc-952d-1dc7e690fb7f | -2.62016 | -48.2915 | 2026-01-07 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9db4c98d-918f-309c-9ecb-53343097adb9 | -1.91472 | -46.95543 | 2026-01-07 04:31:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c9b23ca-c069-3ed1-81ba-d608619cab0d | -2.83862 | -49.12059 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0c69775-3aa2-3d61-adce-9185cc53ce1a | -2.99643 | -54.10536 | 2026-01-07 04:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39778c6c-36d1-395e-8c8d-cc15aa1612f8 | -2.69845 | -48.98922 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| debcb065-3cb5-3842-be87-bc750d3e8942 | -3.62278 | -49.69986 | 2026-01-07 04:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 094f2a69-309b-330f-aa67-48eb5876bbf6 | -2.92611 | -48.22421 | 2026-01-07 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 341205dd-bb59-3f7a-af43-59935f2945da | -1.99731 | -47.3558 | 2026-01-07 04:31:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e695a3e-d906-36c3-8626-935bc2104a79 | -2.89829 | -52.63559 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e84ccc94-e90a-3ea2-8971-fc5386cc12c1 | -2.16573 | -53.6694 | 2026-01-07 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f57b4e01-f2b5-3f82-9f9a-8a1600dfda4a | -2.69504 | -48.98866 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de515cac-dece-3499-8131-b86f1db51918 | -2.73068 | -54.94597 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d68bc52-cce9-31a2-abc2-aaa4df935ed6 | -2.15734 | -51.98497 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aaf55e9-ecc1-39db-8a93-99334b3aedf1 | -2.44356 | -49.02576 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e26f294-6fa0-3101-a68e-b8bc49dcac9d | -0.08946 | -51.28185 | 2026-01-07 04:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaa46230-06de-34b3-b400-9450c886426e | -4.34049 | -45.35038 | 2026-01-07 04:31:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f0eeb25-8004-3006-b239-1701a8f3a80f | -1.91418 | -46.95886 | 2026-01-07 04:31:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a3f2f43-7858-3e1f-935e-4c647aef6f8a | -4.34395 | -45.35091 | 2026-01-07 04:31:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d6806c-1eaf-3bb0-9cf4-d026470c8c9e | -3.43294 | -50.67886 | 2026-01-07 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1ba0e5f-ac49-3676-91f1-2e3f03fb9924 | -3.69726 | -43.43496 | 2026-01-07 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4c9dcbc0-0f98-3aa7-9e7f-2a4f461c0470 | -2.1579 | -51.98149 | 2026-01-07 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0134a9aa-21e5-34e7-ab57-824906fa9d4e | -3.01949 | -48.1097 | 2026-01-07 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2840c4b9-fa20-328b-adbf-8bcf6429032c | -2.79794 | -52.9062 | 2026-01-07 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bacef037-1e07-35e0-bf9e-e4fb05566151 | -1.30003 | -53.90705 | 2026-01-07 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a42a9d9-3938-3b7c-a68d-ec51913774b4 | -3.03186 | -52.85069 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b9ce951-fa25-3ff0-b28b-5c254cb003a6 | -3.42199 | -41.65517 | 2026-01-07 04:31:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 080ff730-3cfb-3b54-9923-4881d04c859c | -2.8746 | -49.11491 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5397097-7d14-3802-94ff-24f13f2de629 | -2.73157 | -54.94062 | 2026-01-07 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f54c5a62-d295-3d6a-92a5-bf8af57294ab | -2.99957 | -52.49924 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 875635f1-51d9-3ca2-b6d7-67015b38a906 | -1.91415 | -53.47473 | 2026-01-07 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7389bd8a-011c-30a7-9f99-12b9f08688b3 | -4.16969 | -40.82876 | 2026-01-07 04:31:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0234b40b-562c-3afc-8330-529e2a9856de | -2.81488 | -54.82124 | 2026-01-07 04:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 668187a2-71b3-3693-8b82-43547acb27dc | -3.4262 | -41.65581 | 2026-01-07 04:31:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d3ee4596-8af8-3479-94d1-f4e4f3183ea5 | -2.36797 | -51.74604 | 2026-01-07 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adefc263-414b-3789-b164-64afe3f82572 | -2.72153 | -49.78903 | 2026-01-07 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd322db4-c5ca-32a8-b441-ad83f3edd115 | -2.92889 | -48.22823 | 2026-01-07 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d8ffba7-0c5a-35fd-9588-b024ce4baf21 | -2.76326 | -49.63976 | 2026-01-07 04:31:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ec851ff-db58-3fd6-83db-48f3317049ee | -2.69261 | -51.85065 | 2026-01-07 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 931a6f1e-fffe-38ff-8c37-f6d4d7091740 | -1.25445 | -53.48713 | 2026-01-07 04:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7244faa0-4768-3842-8379-f6ed672845d8 | -2.69445 | -48.99235 | 2026-01-07 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89b5c012-e196-3bf2-aebd-4acaf2337274 | -2.80849 | -52.94658 | 2026-01-07 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44e28522-8404-3c6d-bb3c-673313ec092b | -4.51656 | -43.69515 | 2026-01-07 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e00275c-863c-366c-9b98-8bd38948c447 | -1.30597 | -54.1513 | 2026-01-07 04:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a142868-91e7-3918-abc1-6e2cabee606c | -3.29299 | -50.35981 | 2026-01-07 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29489aa4-f9d6-3cbb-8d38-00dd9b533e21 | -3.15338 | -48.14124 | 2026-01-07 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e060e467-138c-374d-abd3-3810f4e5ae71 | -2.16499 | -53.67392 | 2026-01-07 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72a9ac3-fa44-3e40-9107-7d341db7c39c | -4.39928 | -43.57513 | 2026-01-07 04:31:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3799c60c-d4fa-3cf5-96e1-ae0709a74d99 | -4.45768 | -44.13309 | 2026-01-07 04:31:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d39282-fd3c-3441-b871-ffe68d6bcd3c | -2.84773 | -52.59365 | 2026-01-07 04:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
