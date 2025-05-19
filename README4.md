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
| 68b47d85-49b3-379b-a2a8-02eddd29cfda | -21.58235 | -48.36427 | 2025-05-19 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18656c3e-5bf2-3725-9297-bc18f1136ccb | -4.28485 | -48.25157 | 2025-05-19 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1de6d33b-b4d0-35b3-867b-1870f95bf5ca | -4.28428 | -48.25551 | 2025-05-19 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1a7ea0-6718-3e00-8dc9-22678526be94 | -12.12829 | -54.66653 | 2025-05-19 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 152ad439-7e7f-3ee2-ab50-05f1916af7b3 | -10.82304 | -56.95417 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ad3d55-06d1-3600-a326-fb98c4a47888 | -12.30007 | -52.47097 | 2025-05-19 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6cb2fda-73d9-362e-a37f-04b0e2cd68ab | -13.30358 | -47.60641 | 2025-05-19 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b18d8e8-e0ff-39c5-ba4a-d6ad7b611334 | -10.82603 | -56.95893 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e76c9bd3-d34d-3346-b807-4a8f7b9b0dee | -11.30901 | -54.02254 | 2025-05-19 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7eefd73-4dd2-351a-ab6f-1df48588e932 | -10.75705 | -57.23049 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91d4c738-3f63-32bd-88ea-cc66ff400b71 | -12.45676 | -57.19052 | 2025-05-19 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c9493a-0b87-37aa-a835-3510df0ffff7 | -12.0343 | -54.97181 | 2025-05-19 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9b51b0f-23d2-3c77-8d8c-54ddc703e676 | -13.04507 | -53.72107 | 2025-05-19 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a8d672c-2305-3970-8ee5-5167180b522c | -13.16025 | -56.82257 | 2025-05-19 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ab15360f-785b-382b-bcf5-e2295527f956 | -13.30559 | -47.60709 | 2025-05-19 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1de7704b-cf23-3301-8745-62bbf34b7fdd | -13.30407 | -47.60201 | 2025-05-19 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35302aa6-a6ec-381b-94df-44975468476e | -12.85975 | -60.22828 | 2025-05-19 05:21:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8f4191a-970b-3f8a-b00e-d75eefe6e195 | -13.04052 | -53.72049 | 2025-05-19 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdf6597d-6664-3835-889e-4b5b4271ab3c | -12.1367 | -54.66776 | 2025-05-19 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4609339-232b-3f69-8b11-43e15096c1b3 | -12.03482 | -54.96813 | 2025-05-19 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b189b1e-991f-3494-8d28-96aad45b64e7 | -10.75798 | -57.2313 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15e96768-8408-31d8-9442-13cdf287959a | -12.46702 | -57.19647 | 2025-05-19 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31bc16cf-4a85-3885-a09c-68307b77c128 | -12.1325 | -54.66715 | 2025-05-19 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f32b2779-3473-3a3e-97bb-04f12691b883 | -10.99167 | -61.64927 | 2025-05-19 05:21:00 | NPP-375D | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22efe77a-5044-3b9d-a84a-fc7c1617ae61 | -13.16398 | -56.82314 | 2025-05-19 05:21:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 91954bd2-60a3-3e92-b203-f71af5a6c2a7 | -13.08862 | -52.28569 | 2025-05-19 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 111c0b61-1230-3731-8fc9-43201c75b160 | -12.29518 | -52.47029 | 2025-05-19 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15be4d40-f831-3dad-a0ae-faa55c5f47f3 | -12.45976 | -57.19536 | 2025-05-19 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad669c7-6052-3d6c-99b8-491f5f3b2b4d | -12.46339 | -57.19592 | 2025-05-19 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0ad4bc3-954b-34c8-a9d4-fae1355f0219 | -9.28794 | -57.54965 | 2025-05-19 05:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d181f415-e28a-3808-b110-80e614f074da | -13.09364 | -52.28637 | 2025-05-19 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f1d4662-bf38-33c7-974a-504467b8b2fe | -10.7586 | -57.22725 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b013e06-e202-3d56-ac74-f368c3362b9d | -12.45613 | -57.19481 | 2025-05-19 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c04dbd0-33ba-3be7-8321-241e6b20934f | -13.30602 | -47.60302 | 2025-05-19 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b30fb9f5-fca1-3cf6-b93e-d8cb1a248b93 | -10.76216 | -57.22779 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9568c7c-dc60-3bde-81a9-e2d9931e4872 | -10.76061 | -57.23104 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 556dcf20-dc74-3884-b14d-d6acaea37232 | -10.75764 | -57.22643 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67ae77c7-4063-3184-ad6f-117ff7b7133d | -9.85843 | -65.26234 | 2025-05-19 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edd99047-154f-316e-8713-92fb11c2d6c2 | -12.03842 | -54.97241 | 2025-05-19 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1866dc2d-ea0e-3e11-942f-bae8adeadab0 | -12.03894 | -54.96873 | 2025-05-19 05:21:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9280f89-a7d8-3438-868a-72075bbabe24 | -10.81882 | -56.95778 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35d4dd93-bdf5-3af4-8e18-eed0764bfa29 | -10.68308 | -57.60707 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e411535-71ad-371d-8772-ce0938d9aa83 | -10.7612 | -57.22698 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92f97591-5a3c-3f71-ba60-df0f4aa0c0b6 | -10.82242 | -56.95834 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebb67564-5654-3a1c-add1-9cb517387e2c | -10.75504 | -57.2267 | 2025-05-19 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c07e8e04-4317-3a45-9413-2c9d395c16d3 | -21.25662 | -48.63732 | 2025-05-19 05:23:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c36c9141-5870-3659-8dc0-6a226817248a | -22.76351 | -50.35828 | 2025-05-19 05:23:00 | NPP-375D | CÂNDIDO MOTA | SÃO PAULO | Brasil | 3510005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d40757dc-3f98-3ffd-8bde-af0de90dbab8 | -21.2561 | -48.64416 | 2025-05-19 05:23:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e040cd52-6257-3608-af20-a29d12733630 | -12.4685 | -57.19524 | 2025-05-19 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ed395e-e6d8-3cad-a02c-23bd8b9ed2c8 | -12.13288 | -54.66991 | 2025-05-19 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e9c4af-0fd4-32ca-99fd-f7a24715a561 | -10.82542 | -56.95718 | 2025-05-19 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98077a8-2eca-3475-9081-402d7d990475 | -12.03513 | -54.96883 | 2025-05-19 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcfb84cb-8798-36b9-bf30-ab42b55fae4f | -12.45767 | -57.19378 | 2025-05-19 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1fd9585c-359a-326e-bb0c-1e44a4d77795 | -13.04708 | -53.72289 | 2025-05-19 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9484c27a-9d62-3ff0-a4a5-c950ccaed951 | -10.75743 | -57.23135 | 2025-05-19 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deff7196-5d97-3eb9-98c6-e0ee5989db6b | -10.76313 | -57.22879 | 2025-05-19 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c7bfe72-b78d-3318-90e5-b3c4facd8051 | -13.03819 | -53.72019 | 2025-05-19 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5c3858a-23ab-37ff-8dc3-0d1641bee72f | -10.75786 | -57.22806 | 2025-05-19 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4364029c-e035-357e-848c-d50409c7a80f | -12.46266 | -57.198 | 2025-05-19 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b275b95a-1dc6-3e04-9cbe-f31c8944616d | -12.13349 | -54.66464 | 2025-05-19 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cada4854-9e55-303d-813b-862ec2d61871 | -12.0346 | -54.97356 | 2025-05-19 05:42:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40e26648-bcaf-3e4a-82d8-df116f7ea121 | -13.04499 | -53.72078 | 2025-05-19 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b8146e7-fa30-3f41-be83-38c4417b61b2 | -12.12716 | -54.66382 | 2025-05-19 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d485d0-064a-3f42-9636-42bac06bead6 | -13.16322 | -56.82413 | 2025-05-19 05:42:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77a88550-9d71-38f7-a4d1-b9eb2786d534 | -9.85925 | -65.26073 | 2025-05-19 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8820aa0-015f-3358-b9d8-9a1f97158d88 | -10.05286 | -64.99277 | 2025-05-19 05:42:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b180b9f-b9c3-31f5-a706-66fb85067309 | -9.66318 | -65.75432 | 2025-05-19 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7c957dc3-69ba-3f39-b0f9-e867472dab12 | -13.04028 | -53.72229 | 2025-05-19 05:42:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b45a953d-ca65-350b-bd6f-a83aa5d95f2a | -12.45811 | -57.19019 | 2025-05-19 05:42:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c24132f2-36c2-35f8-8776-d17e5844771e | -10.82006 | -56.95631 | 2025-05-19 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c917fb41-3e57-348b-b95a-4394daabfb15 | -12.12656 | -54.66905 | 2025-05-19 05:42:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8064e29-55f9-3dc4-8e9a-fbaa24165aae | -20.71511 | -54.41897 | 2025-05-19 05:44:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4536f32a-c444-32fd-a73a-8b0a1d22de88 | -10.7576 | -57.23098 | 2025-05-19 06:25:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e97ea51c-22b2-354e-984d-3b3db49e9f4e | -10.75892 | -57.222 | 2025-05-19 06:25:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f8b90b9b-9567-3bf6-8744-39ab2aa93620 | -13.16104 | -56.81911 | 2025-05-19 06:25:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7a3b32ea-3b13-37cc-8454-1d7f4f587080 | -12.461 | -57.1879 | 2025-05-19 10:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| b53d68e9-2f00-3e68-84d8-46445af0ce2e | -12.461 | -57.1879 | 2025-05-19 11:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 608cc24f-517e-3224-af6b-1b7847f1835b | -12.4608 | -57.2079 | 2025-05-19 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| fcdb7873-8633-3c37-9cb1-286ed52ce1c3 | -12.48 | -57.1863 | 2025-05-19 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| b03ce3e5-bacf-381a-b61e-e9898284d719 | -12.461 | -57.1879 | 2025-05-19 11:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 188.1 |
| 4719a2b5-5c9e-34fe-8858-86df656b5651 | -12.48 | -57.1863 | 2025-05-19 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 3c3c6d13-f953-30c2-abff-6bffb35b7d0a | -12.4608 | -57.2079 | 2025-05-19 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| b11336e7-cb32-3d60-9780-b7cb831aaa8b | -12.461 | -57.1879 | 2025-05-19 11:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 264.8 |
| 415479bc-e370-3960-9eef-183a1150109d | -12.48 | -57.1863 | 2025-05-19 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 8c3a8cad-3970-39fb-9ac6-3c337392f4d1 | -12.4608 | -57.2079 | 2025-05-19 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 147.9 |
| b530cffa-07ac-36cc-bac3-9722cb1f7701 | -12.461 | -57.1879 | 2025-05-19 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 393.1 |
| 43041098-bb95-3a03-a7ca-28ba16d6bc91 | -12.48 | -57.1863 | 2025-05-19 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 259.4 |
| 18ffacf4-65ab-3c78-9b40-b1b5ee55ced8 | -12.4608 | -57.2079 | 2025-05-19 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 8ec1a257-358c-31d9-821b-2b22412cc921 | -12.461 | -57.1879 | 2025-05-19 11:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 433.5 |
| 958544d5-fe37-3ae8-b6b3-563eba44a3a9 | -14.4064 | -46.02732 | 2025-05-19 11:45:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 56601e7f-e93e-33f8-8a0f-5cd642c8dd29 | -14.40643 | -46.05388 | 2025-05-19 11:45:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e8e9b422-4aab-3304-80ec-6e0bd3f24658 | -12.4608 | -57.2079 | 2025-05-19 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 61878caa-f7de-39cf-b7b3-df7422addfa1 | -12.4613 | -57.1679 | 2025-05-19 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 438fc6f7-943d-3dd5-828c-3051c59e5dae | -12.48 | -57.1863 | 2025-05-19 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 207.8 |
| 6cb7cf4c-8539-3cb1-a188-80868867071d | -12.461 | -57.1879 | 2025-05-19 11:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 417.5 |
| 8f02f2e2-4029-3cf6-9d43-46a07e205390 | -12.48 | -57.1863 | 2025-05-19 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 173.8 |
| b609cc05-6d73-38ab-b240-5d66cdaba679 | -12.461 | -57.1879 | 2025-05-19 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 430.0 |
| c42f8c6f-7674-34ce-a1f9-48c4c433a6e5 | -12.4613 | -57.1679 | 2025-05-19 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 47d212ad-2b87-3a32-a7d6-6c0ba1c6dd8e | -12.4608 | -57.2079 | 2025-05-19 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 210.0 |
| a05cac49-1b58-3dbc-ba76-2f3bd5cfac23 | -12.48 | -57.1863 | 2025-05-19 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 224.8 |


[Clique aqui para ver as próximas entradas](README5.md)
