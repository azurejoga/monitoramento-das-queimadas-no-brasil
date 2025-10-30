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
| eb0588a5-71f0-36db-8448-63b5548ec635 | -12.25334 | -47.94251 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5d72fc72-36fd-37a1-b00e-24246a522543 | -10.86046 | -47.8665 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc85b5ac-fce3-372c-8bd4-7a1c9dc66fcc | -14.23202 | -44.33201 | 2025-10-30 00:33:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e26037cc-209e-33f6-8b3c-e4edd2c68dfa | -12.8727 | -54.74847 | 2025-10-30 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a231705c-42fb-3a21-8680-2a485558f16c | -11.08386 | -49.87069 | 2025-10-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5519b1e0-fb95-3076-889d-22eeebd6abee | -16.27981 | -45.87659 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a19a78bd-944e-3130-a58c-55660c469bf4 | -14.77576 | -44.99476 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c06f1f8f-381e-383b-9866-163e9dc8b260 | -12.54386 | -49.57449 | 2025-10-30 00:33:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 07bd82b0-3949-32b4-999a-d53b90ca8307 | -11.95764 | -49.93674 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6ba8a50f-526f-3248-b3f4-52197b9ffae6 | -14.77228 | -44.97157 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 94e49f93-a568-3b49-a03c-7a5c592b372d | -12.00597 | -49.95211 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec19b635-5273-3304-aee1-2d01771f5253 | -12.18152 | -47.75636 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 03f2dd10-518e-3660-8dbc-4fdb3309c6e8 | -13.46972 | -47.99976 | 2025-10-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ede5d949-c533-3bd6-a3ae-5589361646a4 | -14.31743 | -48.00273 | 2025-10-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 03e57f7b-537a-33e0-9d33-c9ff8fc052ab | -12.18021 | -47.74713 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 810e5861-8830-3afb-a253-5742b51e1259 | -13.36328 | -43.09625 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 35.7 |
| 8d3a841f-5837-390e-8022-ce930a1b2d08 | -9.90404 | -44.89834 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e65367f6-5952-3680-9f36-0aff6f2add44 | -15.58864 | -43.16018 | 2025-10-30 00:33:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 918c4798-5f9f-3ae7-aea9-b8faf73ae29d | -11.55306 | -44.68913 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 583b45cd-6716-3c80-b8ea-4978456dfb88 | -12.28601 | -47.00517 | 2025-10-30 00:33:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e97e6ded-5664-3839-8aa7-8f219e545799 | -12.15445 | -47.69465 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 95d35905-01d6-3056-931c-b28466b7d31c | -11.96577 | -43.27963 | 2025-10-30 00:33:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 44376188-634f-30b6-bef6-9eeb37f089e9 | -13.07473 | -48.20942 | 2025-10-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| bda82f8d-f3e0-3219-a3cb-2e2467a836d0 | -12.87047 | -48.66335 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75476963-e753-3696-8766-b330ab494a41 | -13.40212 | -48.38238 | 2025-10-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ef3b3c1-1069-32bc-8761-18548022aad4 | -11.04192 | -47.84624 | 2025-10-30 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e87157f-5343-3933-bce7-fa1b200da677 | -12.64319 | -47.8904 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 98257e24-a76d-3686-816f-3d61e548528c | -14.7858 | -44.98667 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 3861b831-d438-344e-97f9-dd5b7717cf53 | -10.36123 | -47.27701 | 2025-10-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9636a0cd-9146-3806-9fb7-1c21a447f601 | -13.36487 | -43.08572 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 0e4af463-08ef-3f6b-a2a9-6c60306ab9d5 | -13.37747 | -47.4201 | 2025-10-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cda5edea-c64a-3068-a1ca-df08bc652d2f | -10.99077 | -47.87311 | 2025-10-30 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 25055fb0-056b-3472-8fea-ccda3fa8cbc3 | -12.32642 | -48.0647 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 86544975-e844-36f3-8a79-d8f5c452af48 | -11.06321 | -50.33363 | 2025-10-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f40cd91-1cd0-33e1-b760-6d67e77f49f3 | -10.47955 | -45.04356 | 2025-10-30 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 661280ae-0458-3ed6-be3e-267d5b91e9bf | -12.32515 | -48.05568 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 56dd0e72-41e4-3341-b49c-66b42df3fa89 | -13.64883 | -48.42869 | 2025-10-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 15cd8ac0-19dd-3660-b912-481c31907f5a | -13.20271 | -44.48565 | 2025-10-30 00:33:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5468877b-00e2-304f-bc96-86ad1d4ba95a | -13.98325 | -44.02332 | 2025-10-30 00:33:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 1adb831a-6a66-3908-a2d9-5e6fcc1b5db5 | -10.36122 | -48.70074 | 2025-10-30 00:33:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 06dc92ab-49b3-31fa-8911-fa3161768400 | -13.5294 | -44.35249 | 2025-10-30 00:33:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c2c723bb-65ae-3c90-8474-033937a029f4 | -13.40086 | -48.37335 | 2025-10-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2a4afa5d-2e6b-30ee-b153-2a41dc489a09 | -13.71385 | -48.76992 | 2025-10-30 00:33:00 | TERRA_M-M | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 52499cd5-8316-334d-b400-d3bc8127ad77 | -10.28193 | -44.57831 | 2025-10-30 00:33:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9bbf9323-1b88-3024-9aaf-4c6911e9541d | -15.24968 | -43.12922 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 43d16269-d0ef-39da-a430-d7c01d586f25 | -10.3341 | -47.08985 | 2025-10-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c8ec6818-0a79-3e99-b87d-1f91eb0780f0 | -15.82252 | -42.68462 | 2025-10-30 00:33:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 188c4fbe-2a28-3fd9-85c1-0ad75d7c8ffb | -10.48809 | -45.02877 | 2025-10-30 00:33:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4cd527de-2218-3d48-82b3-3ddf1f2f49cb | -12.87679 | -54.76169 | 2025-10-30 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| f78ee0e8-67b1-3602-b4f4-342a7f31f947 | -12.66613 | -47.34203 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 989bad47-ad35-3899-a413-b0e7d1199ac4 | -13.21874 | -47.72968 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2e322896-f816-3cd5-b6bb-74b443d63deb | -14.77413 | -44.9768 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cb92ac96-ed60-3ff8-b2ec-d52ad5b18e6e | -9.84313 | -44.88559 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| fad370db-6029-3ccc-91dd-4e07d33d9cae | -13.18166 | -48.44582 | 2025-10-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 65612279-e762-34fe-90fa-1321727e5559 | -13.47857 | -47.99841 | 2025-10-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 296ff264-e174-3ea5-8be3-ab8c231a1d6f | -11.23762 | -49.78078 | 2025-10-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 223f2156-2b06-31d3-b08c-8bbb3279ec75 | -13.28269 | -47.72372 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0d993dbc-4845-396b-bc2a-b0f7a3bc410e | -11.20473 | -47.56538 | 2025-10-30 00:33:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 635d0206-32e5-3f0e-b634-108fd8d739e3 | -12.81287 | -43.46315 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a1f058fb-c8e4-3016-aa87-a622aef5c322 | -12.19553 | -46.70718 | 2025-10-30 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 85cb8b06-6eba-3b11-8947-798f04038696 | -12.88564 | -48.64272 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5876e1ca-bb6c-3275-bbc6-c435898ec640 | -12.87681 | -48.64402 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 285a7a5f-bd32-39c5-b126-ff0ca71d1283 | -13.74579 | -48.39917 | 2025-10-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27e305d9-1125-33f9-bacb-d21cc6c5ec8c | -9.49947 | -40.39049 | 2025-10-30 00:33:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| ab708079-bd5c-3761-8f03-b6f00b1f1560 | -10.65092 | -48.79585 | 2025-10-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 47871510-0d97-35e1-93f8-b96c40406327 | -12.22695 | -46.46481 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dd0bfd8c-b936-395f-b797-bf19cbe3e7f3 | -14.223 | -48.11585 | 2025-10-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2d49423b-9983-3020-85b3-69d22da1cec6 | -10.93431 | -47.80225 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8d76cbcd-95fd-3e16-b0db-33fb10a8d923 | -10.65217 | -48.80479 | 2025-10-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83782686-3b89-31b6-b50e-025619598f56 | -12.01163 | -47.79408 | 2025-10-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3863af9f-4af2-3e35-91ac-5ad840da3196 | -15.58867 | -43.15372 | 2025-10-30 00:33:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cf16217b-7be3-354c-8f1b-6d6b2be210b3 | -15.08551 | -41.98967 | 2025-10-30 00:33:00 | TERRA_M-M | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 31.6 |
| 78136de5-084b-3cb6-99e2-0d719908cf00 | -12.83319 | -43.44355 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 093dca3f-4339-32a7-a900-9f9370d895f6 | -10.95922 | -48.04333 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e9083346-fc76-3e96-8e75-9255a9d970fb | -12.30648 | -50.27736 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c419b3a1-94a1-3d5e-8a63-90bf41efad42 | -13.29952 | -47.06698 | 2025-10-30 00:33:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5d0ccab1-a009-3c1c-9318-eaf7ec22f8b7 | -12.50411 | -50.58136 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| c37fe1d7-28fb-3b59-b26b-c4541a180fe5 | -14.98186 | -43.39456 | 2025-10-30 00:33:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 8f9f7525-0431-3de9-bec6-a5c17b708f53 | -11.84584 | -47.92481 | 2025-10-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 7c36a424-a523-3542-9dcb-385854c57175 | -12.88439 | -48.6337 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1682d14d-950a-3cde-b0f9-98e84ea3b2c8 | -12.83569 | -43.45925 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fc0d1dda-09dc-3d2e-86d2-3a4654e23540 | -14.77402 | -44.98317 | 2025-10-30 00:33:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1e772e0c-a003-371c-9dbc-c3d4f5e10383 | -12.31629 | -48.05711 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e31a8523-b131-32f2-8d67-0b077091a551 | -10.86119 | -47.61237 | 2025-10-30 00:33:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3a093d24-76e9-3245-8e45-238bed015e80 | -12.14495 | -48.02026 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f802fc1a-862f-3855-a0ba-bb6fafedebf4 | -13.24575 | -47.71963 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6aad957-18bd-3360-ae6e-eec5baa421c2 | -10.25346 | -43.95358 | 2025-10-30 00:33:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 95a82996-efe5-3abc-9556-13f4dfc45569 | -11.91188 | -44.17371 | 2025-10-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 77bfa89b-6398-3c1c-8db4-0795c0ec57da | -12.18625 | -46.70865 | 2025-10-30 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4a21f49f-ea21-3d71-ac7c-e2ebd7c295d4 | -12.53848 | -47.54548 | 2025-10-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d7f2fe6-d410-3576-90e3-cda084197b07 | -12.11217 | -47.1427 | 2025-10-30 00:33:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 713938a4-7f5c-325e-bbce-c2ca03432893 | -13.59324 | -42.28786 | 2025-10-30 00:33:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 0b43b4bb-df75-3d0c-8f01-c055eccd021c | -11.46125 | -48.53041 | 2025-10-30 00:33:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d6c85e39-f3cd-32c5-9978-03c02809aa5d | -12.23332 | -46.46786 | 2025-10-30 00:33:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b98d71fc-bd90-361c-8161-16066afcdeb5 | -12.82177 | -43.44551 | 2025-10-30 00:33:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6d903d67-caa3-309d-ab19-284731cd0cb9 | -13.60862 | -48.41323 | 2025-10-30 00:33:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b23bfaed-043f-347a-b09b-e0baf4bf4674 | -13.36056 | -43.07988 | 2025-10-30 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| e4407213-7e48-3c25-bd8d-1e495e1551f0 | -12.69298 | -48.64646 | 2025-10-30 00:33:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f25a1486-e55a-3afa-91f3-3096cfaa0dc7 | -12.29781 | -50.27472 | 2025-10-30 00:33:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cfc30e0e-b9e2-3534-8924-f5897c759101 | -11.82301 | -42.80944 | 2025-10-30 00:33:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |


[Clique aqui para ver as próximas entradas](README4.md)
