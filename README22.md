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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 485f4a68-3902-31d8-bf34-2cb510b1095e | -3.95148 | -49.35085 | 2025-10-23 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b3408ec-39dc-3f61-9d39-057140a295a2 | -9.23839 | -45.59783 | 2025-10-23 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2432dc9-d082-3800-a9e7-075e61ffe83b | -10.61583 | -45.1847 | 2025-10-23 04:38:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87a24a39-376c-3aca-a06a-56a089c3b9b2 | -11.9972 | -46.78136 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44b09462-03b9-3204-a64a-3569c35befd8 | -10.96543 | -50.26333 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4018d661-efe2-359c-8a45-3ef7621eb7ab | -15.59494 | -45.91267 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb686d1b-f3d6-35ae-9988-787b61f74b22 | -12.77415 | -47.38275 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94c392eb-235f-344f-bd25-0fcb7def9ff4 | -9.86856 | -47.71318 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 79b6d665-88f3-32ab-8278-a05ee9eca24c | -13.21077 | -47.7462 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 629e757d-0535-3b12-b2fe-f5133e293c28 | -12.67261 | -48.64125 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17cf8a0c-f5e5-38c9-a869-360525432d9f | -15.10338 | -48.52677 | 2025-10-23 04:38:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 401dd920-a1f1-3328-a9f6-cd7a70a6ec26 | -11.9937 | -46.78083 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f53bc613-5913-3e4d-816a-ff55d75c1a1e | -16.30549 | -45.87778 | 2025-10-23 04:38:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b389ccb8-0b9c-3d6b-83c8-3b2a7c8a20bf | -10.39097 | -47.10155 | 2025-10-23 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb80257-8bc5-3e54-a339-dbc66a222c7b | -14.39361 | -52.77211 | 2025-10-23 04:38:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00a66a5b-a01d-3680-8644-f36328a72cf1 | -9.93089 | -47.46552 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad8ec3bb-ace5-31f5-9379-e9b1135635cd | -10.21078 | -46.64312 | 2025-10-23 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a9534f6-3949-32c5-a748-fe29419bfd9a | -11.00775 | -47.67334 | 2025-10-23 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee102ae3-ceb2-3bf7-8cad-1c906a20f112 | -13.89291 | -48.37161 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 088881f4-4deb-3cd9-8aab-c27ad54e6ec3 | -14.84329 | -54.2244 | 2025-10-23 04:38:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d287b16c-6729-3182-8dee-9188c58e77a9 | -14.83205 | -48.31427 | 2025-10-23 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 308f3717-3bfd-3366-bc03-77509de2470e | -12.80715 | -51.3296 | 2025-10-23 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a1630b9-4a1a-3af5-b504-4ca98bf35192 | -10.02379 | -47.0648 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 166b4ff6-b586-3744-bcda-548deb66c573 | -11.89119 | -49.89892 | 2025-10-23 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9dc70c16-ea33-3b66-a4d4-7d2b7e2c66f1 | -9.86411 | -47.71977 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd64f8a6-f594-316a-9e08-0baf28d9b2df | -15.79086 | -44.48926 | 2025-10-23 04:38:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56e68b1e-f015-347e-8dd1-ed86b093f777 | -13.29973 | -47.48132 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6db84e42-e997-319d-9219-eeab80cd7fa2 | -9.97266 | -47.07956 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de21e2c5-67fc-39c8-abb5-bdc27e195e7e | -15.67455 | -53.34573 | 2025-10-23 04:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 036db129-7e4e-3182-b26b-e0a6dc240b56 | -10.39327 | -47.10943 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d0a9ec5-e45f-3273-974a-341abc2ddbc0 | -15.59693 | -45.89854 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 774a00fe-88be-3020-b3bb-1362ace65d5f | -10.38755 | -47.10098 | 2025-10-23 04:38:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dcae072-3f11-308d-86af-716b88dd1294 | -14.87392 | -59.63834 | 2025-10-23 04:38:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a628ea18-19e4-33aa-8627-0ada5adac648 | -12.76783 | -47.37786 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 886fd4f8-c60e-399a-8405-b1c6b57024ba | -13.79124 | -52.77567 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0838a7da-77c8-34bf-834e-7535a3181d94 | -15.59428 | -45.91737 | 2025-10-23 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a78d722-1f36-35a6-8b3e-787b8957d02c | -11.69423 | -43.93089 | 2025-10-23 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ec98003-95a8-3f34-a376-51e97efcbbee | -12.67203 | -48.62288 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29858059-0766-3e54-b12a-5aaf9b2bc6b2 | -11.00775 | -47.67335 | 2025-10-23 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc2787eb-5f28-3f68-8af0-cdd2ae1718c8 | -11.00161 | -47.80238 | 2025-10-23 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0879eb16-1d61-30fa-835f-260e537ea160 | -12.67816 | -48.62756 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45a69c6a-9702-374e-ba07-8d58e88feec7 | -14.20918 | -44.52328 | 2025-10-23 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5d2de22-d09e-399f-b788-15665c71c264 | -10.27545 | -47.58215 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 933ebf16-2b00-3d14-a1a1-a3eb73265930 | -13.04677 | -47.21928 | 2025-10-23 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b36c14ac-a25f-36ed-b565-969791aec28f | -12.76783 | -47.37785 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f358ce76-81cd-37b2-b352-e8ba7ce95b9a | -14.836 | -48.31425 | 2025-10-23 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37d838e8-50bd-347b-a383-68f0e7fe702a | -12.00247 | -46.77009 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ce049d-9920-3671-a713-b119650c40f7 | -12.16594 | -47.04928 | 2025-10-23 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99db0a31-c356-322a-b126-5978c97aced7 | -11.99428 | -46.7769 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0261d956-7277-349a-a0af-716ee9df5ecd | -11.99661 | -46.78527 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 39a200d7-717f-3382-a5ee-ad1c6ab8d99c | -13.59737 | -43.47739 | 2025-10-23 04:38:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eccfa9ba-3390-3226-b505-3082af2f0324 | -13.18526 | -47.7541 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2a490dd-b53e-3c41-86a5-4e7ad5f9f575 | -11.36457 | -49.78703 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 456703cf-4bdd-3db7-a639-9750bde820df | -13.79497 | -52.77383 | 2025-10-23 04:38:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3462053f-4cdc-32db-be07-fa7e22697a4e | -11.00161 | -47.80237 | 2025-10-23 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be1a7126-45f9-3bcb-beb9-3de6a4778faa | -11.70711 | -51.12851 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a8066a4f-bb5a-326c-a27e-db6786e14acc | -12.00538 | -46.77457 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d32ac9d0-99a9-3fe8-bb8b-0c501f032839 | -12.0042 | -46.78244 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba3a62f6-033c-3d61-9b8e-43e0db8b1226 | -11.35517 | -49.78935 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f26c2d6-4f67-356d-a13f-646232d6e8ab | -10.91283 | -50.11381 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67b0c33a-10b7-337f-830d-a531880e26b5 | -9.86747 | -47.72029 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae41326c-e310-3920-a52e-654048546bc7 | -11.53851 | -52.24017 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59443610-4fd5-3d70-9dac-2e90e84d8002 | -11.34363 | -51.44617 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7cf61908-1b6d-3296-a05e-b11453d39717 | -13.37459 | -47.26698 | 2025-10-23 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aabeb71f-46c0-31a9-b011-41f3fb559c1e | -12.78278 | -48.51608 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae9a35fd-59c6-3dcf-ad94-9fea6c00f097 | -12.35316 | -47.88432 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50852468-4900-354c-b109-85b2d707aef6 | -11.35893 | -49.8007 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7a36e8a1-adf3-3598-a9c2-68f937fdb952 | -10.90916 | -50.15771 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ae13d64-0adc-3586-bd75-3f9e8a00e92f | -9.9755 | -47.08379 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e4b17c3-bb67-3d49-8999-c262be1cdc31 | -9.93049 | -47.5798 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ea021a5-8bcd-3358-b0b6-4490c0c849e5 | -13.32878 | -47.95553 | 2025-10-23 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13fece92-89da-37c7-8916-d1f0d46f65e0 | -11.99311 | -46.78474 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 91e663e9-a7e6-32e4-9c41-3ac5b29643bc | -12.68987 | -48.64037 | 2025-10-23 04:38:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 037e6c1c-4315-388e-9d2d-a3cd8813049d | -12.24955 | -49.59028 | 2025-10-23 04:38:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 324f8679-fb62-3e13-bab3-dd82eb5d04c3 | -12.16536 | -47.02948 | 2025-10-23 04:38:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69555039-36c4-3dd6-9777-61ee409c7b0f | -11.3568 | -49.80058 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 47a0d0a3-b622-3538-a7a9-7a2ec0a2db0f | -13.89628 | -48.37222 | 2025-10-23 04:38:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bca77d57-cbb4-32a3-a113-a5b58a0a338e | -9.92751 | -47.46499 | 2025-10-23 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95fc8645-2409-3efd-9abe-235723c53481 | -13.01134 | -48.45967 | 2025-10-23 04:38:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4c1a148-919c-3ef0-adb4-a6b2f003ea0f | -12.09585 | -63.62298 | 2025-10-23 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ad6a712-6eae-3f0e-b392-f33d73a800f0 | -11.36008 | -49.79359 | 2025-10-23 04:38:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8dcd6e0e-5fbf-391c-901a-cc5c5803285a | -9.97775 | -47.06904 | 2025-10-23 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa60e192-1c39-36bd-91e6-5f8febe25003 | -12.01775 | -46.73997 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21078103-f73d-3233-8f65-b40cbcc0f507 | -12.24196 | -46.78104 | 2025-10-23 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c25a3d53-e3a9-3e0c-bf17-a9171498cfce | -11.9902 | -46.78029 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cf3c47e-1cf8-3594-8db0-d5348c524769 | -12.91131 | -47.7429 | 2025-10-23 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c225d6b8-ace9-3424-bd2a-593353a4acf3 | -10.24997 | -47.99923 | 2025-10-23 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 177c3748-f9c2-3977-a7fb-c9c5310962f8 | -11.49519 | -48.47219 | 2025-10-23 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1a0c1a3-3c52-33e2-aef4-c8bd2372c88a | -12.37693 | -63.86929 | 2025-10-23 04:38:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 515ccb3b-0375-3640-b2e4-67a9d0f7b42f | -10.48788 | -51.87025 | 2025-10-23 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e020643a-24e3-3d15-8774-718ef6e44b52 | -10.03673 | -48.71545 | 2025-10-23 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e85616-f84f-3e1a-b48c-6bcda99e5316 | -16.51531 | -51.39988 | 2025-10-23 04:38:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c7d43b8-71b5-32f1-8cf6-bd41c3faf88b | -16.08039 | -51.40843 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72adddd3-2003-3240-a73c-e7bb39ca7d60 | -14.84401 | -54.22627 | 2025-10-23 04:38:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b74d54c0-a529-373c-a594-4289fd7047c0 | -13.0375 | -47.23364 | 2025-10-23 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07d5153f-0b8e-304d-8243-358d55f92afc | -10.63816 | -42.30584 | 2025-10-23 04:38:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 492b04c1-117e-30b1-9ef7-54fddacb288c | -16.08315 | -51.41273 | 2025-10-23 04:38:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc9738d8-185f-3f08-939f-c03f3b18d323 | -16.30549 | -45.87777 | 2025-10-23 04:38:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7af4562-1abf-322e-9bef-f99d1cdfcdbd | -11.74309 | -51.18947 | 2025-10-23 04:38:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29af1bde-5ddc-31c0-95f6-5a0ce465d8ad | -12.00129 | -46.77797 | 2025-10-23 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README23.md)
