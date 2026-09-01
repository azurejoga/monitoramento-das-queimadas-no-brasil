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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 636e7be8-fc35-3953-9e8f-b102ad40ccc1 | -10.18394 | -50.33486 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 20b21333-2485-3f7b-b115-be57427e5ab2 | -19.15711 | -57.36031 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| cbadd1c0-aa03-3fbf-8a55-dea9ce0dc1e6 | -16.0441 | -54.39667 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 58e8cc7d-272d-3854-87b7-95d896a739a4 | -15.66001 | -48.70454 | 2026-09-01 00:24:00 | TERRA_M-M | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| cbd9dd6d-667f-3e4f-a20e-c045da7148bd | -10.74752 | -54.0695 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f32a5b71-7513-350e-80c3-63750e9a90e0 | -10.73628 | -47.98564 | 2026-09-01 00:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 789f62e0-c799-3a91-940f-6eb054eb7dd1 | -10.15593 | -50.29676 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 4c3a384b-9e14-3645-b9e5-0a4e79368c87 | -11.25797 | -50.5857 | 2026-09-01 00:24:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 28441682-d7e4-39d3-a95a-adb5d7ce6577 | -19.17719 | -57.34307 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.1 |
| 0e4a33bc-336a-39a1-b4af-457a4ff7f4dc | -9.21332 | -48.01017 | 2026-09-01 00:24:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 350e707f-f28f-3da1-a491-458c1a2d1adb | -10.1689 | -50.30891 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| eb1410fd-e7ba-33d9-b905-70a7c3c87617 | -15.25013 | -53.84132 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c44ea756-123b-362b-add0-209ee6720e47 | -15.64554 | -50.11279 | 2026-09-01 00:24:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 589f091e-76c4-37ff-89b2-90bd373e073c | -10.04031 | -44.68897 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d5a57757-fdfa-3298-b0ec-b256327ad20c | -9.98224 | -53.93628 | 2026-09-01 00:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 23f055e2-cd43-317b-967c-e99469a809a5 | -17.18145 | -54.29411 | 2026-09-01 00:24:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ed0a3c3-4eb9-35b2-b903-a59939b3f05c | -14.38595 | -52.53559 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bfa36c13-49dc-3de3-bebf-c1e56da61903 | -14.26137 | -52.89158 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1eff9eb2-fa10-3c12-98ab-86edad9f5cd8 | -14.71772 | -53.58122 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b6b32215-381f-37e4-bce0-bb05d5b0296b | -10.19474 | -50.33313 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 417.5 |
| 36aa7891-2e1c-3fff-9d87-ee305a6d5f72 | -15.39644 | -53.761 | 2026-09-01 00:24:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 899a09aa-a4c0-3f97-bb35-210eaf36252e | -10.75259 | -54.04129 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5faee6ec-0aba-3a5a-b798-ff56b100b392 | -11.19921 | -45.10777 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 0b076718-3094-30c5-8ff0-115d18570704 | -14.9884 | -48.12695 | 2026-09-01 00:24:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| fa90376e-865e-3d03-8376-1b15b3f11d2c | -10.9506 | -49.77652 | 2026-09-01 00:24:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 64bf3487-c3a7-3d63-8439-b95b354ae7f9 | -16.14435 | -52.38638 | 2026-09-01 00:24:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 8bc3fe8f-57bc-3a53-900b-2aa49742dbf3 | -14.58454 | -54.08391 | 2026-09-01 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 69f76fc7-bce9-3bcd-a359-3130da339a80 | -15.404 | -53.7506 | 2026-09-01 00:24:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf2d8fda-00b5-33c7-879d-63eece2d2918 | -12.103 | -44.98796 | 2026-09-01 00:24:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| be1f6288-455e-37f4-a5dc-334c69f91908 | -14.69384 | -53.53857 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| fdbab3ed-e347-337f-ae9f-1f8a82ba292a | -10.14257 | -50.30522 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 278797eb-79bc-3869-b4a5-d2411ecc882c | -19.20147 | -57.33374 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.5 |
| d4b88cc9-8c96-364f-acb3-0159cf1e548a | -19.19219 | -57.34961 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 8a4adf1c-a556-3e0e-9d19-a27501a1b1b4 | -11.48518 | -45.07322 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| aadf9c29-e139-37a1-bfd7-017a2b871672 | -14.39223 | -52.51536 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7e3a34a3-eba4-3d8a-9277-0a5e636775f0 | -10.82836 | -50.72366 | 2026-09-01 00:24:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 76cc1cb5-e9c9-32ec-8b0c-de3a215475a9 | -16.06192 | -54.39415 | 2026-09-01 00:24:00 | TERRA_M-M | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 728edecd-3750-3318-81b8-c778ac10d09a | -11.11361 | -51.54108 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5f9a123e-5155-3ad5-b97a-7171ca2992a8 | -14.25875 | -52.87307 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 55b7c94b-878c-3368-95fa-3b5767c51fc2 | -18.51695 | -48.23502 | 2026-09-01 00:24:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 97fbdd81-0a39-32d1-a186-f85f6fe00418 | -16.0671 | -52.16671 | 2026-09-01 00:24:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 77be8600-2d43-36bb-98cb-c3a6427e837d | -19.17887 | -57.35755 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 7749255a-f398-3d0f-87c0-252573a11561 | -15.43144 | -52.68945 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 54bd8aa9-d61f-312b-96dc-d1741efed745 | -19.24495 | -57.32821 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 6684c66e-e58d-3c05-9ed9-e32c9e258ace | -11.10865 | -51.5075 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| f204b20c-4bb7-37c2-99ec-a76561329919 | -10.19683 | -50.34692 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 330.0 |
| c330a660-5935-30e7-9c69-075923e74568 | -14.39986 | -52.50448 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d02d77f-ed64-3a24-9779-405bc9d47ecc | -15.61035 | -56.38939 | 2026-09-01 00:24:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c3f1ae35-6672-39e0-9424-0995ee310d62 | -15.29079 | -53.19253 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 948940a2-d97c-3f3f-86ee-d325d3f62a08 | -10.20969 | -50.35897 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 2a436cae-29e6-34fd-b653-66ce016f3ef4 | -11.20714 | -45.11192 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 4178cbaf-571b-381b-83d3-536e05d08923 | -14.11911 | -52.79659 | 2026-09-01 00:24:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2aca1fd7-1aa3-329c-8702-a4006b8e4179 | -10.02352 | -44.69195 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 265.3 |
| 551b2e94-c211-347e-a970-06ad3f9ae623 | -11.17487 | -55.1008 | 2026-09-01 00:24:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99d82ac8-66c6-3942-9681-22615206fef8 | -17.386 | -42.3419 | 2026-09-01 00:24:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 213.6 |
| 4355db34-df2f-35d5-a683-305c79cdba78 | -16.57102 | -52.52763 | 2026-09-01 00:24:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a72bc7f4-15a2-37cc-b7b4-fd4677ae643e | -14.27917 | -52.88887 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0ff2f3c9-c6a6-3c3a-82fd-c50025cc3fb9 | -10.18815 | -50.36242 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 225d6340-e1c3-3171-bd20-6f3efa72de69 | -16.18912 | -49.33142 | 2026-09-01 00:24:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 190c7fee-3a04-36a6-9fcd-c31e47be4065 | -15.85251 | -47.69728 | 2026-09-01 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.5 |
| fb635255-96ba-33b2-8e80-dafe73065753 | -16.47226 | -47.94983 | 2026-09-01 00:24:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e5b0d986-a158-311f-8722-25783c58119e | -15.75695 | -56.091 | 2026-09-01 00:24:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 8ae160ca-c294-3034-87a0-3151bdabd3d5 | -11.49117 | -45.10684 | 2026-09-01 00:24:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 56bbcc77-d2ea-31e4-ad33-4ca427be10d2 | -19.21234 | -57.33236 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.1 |
| 7cbaa41c-8a02-30db-80df-35eb3f2b1277 | -11.05971 | -51.51512 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67b2c251-b826-3ebb-b577-4a4f54a77718 | -13.48185 | -57.07136 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5424875e-a45c-3b6f-b691-590a8e01bf5f | -14.7039 | -53.5463 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 36f2a496-137b-3a9a-8d51-7d74b011b065 | -16.57857 | -52.51697 | 2026-09-01 00:24:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d09211d-3e88-3d21-8fb0-6d97658bbca7 | -13.44693 | -57.048 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7aab2585-81d2-3b53-b7e8-d984e12bb19d | -11.30537 | -45.18685 | 2026-09-01 00:24:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 43c1c90a-3b43-3c9d-912f-321b23f2e278 | -10.73957 | -48.00599 | 2026-09-01 00:24:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dff5e31a-c4d4-339f-86cd-bba38600397a | -11.24803 | -54.01451 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 00eca73f-e4a6-34e4-a963-8283933bdbd9 | -15.40248 | -52.7412 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 91001cce-9285-306c-a94c-f1f41b380156 | -11.07286 | -51.53595 | 2026-09-01 00:24:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 6cfaaed1-7e73-34f7-aa67-9ed8361ddea1 | -10.74126 | -54.02461 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f7adc6cf-170b-3c2f-8d3d-91550309d628 | -10.74251 | -54.03358 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 664c56a2-4ccf-3529-8b9b-70e5505c8c86 | -10.8446 | -54.04022 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e6eeb2d1-9746-3692-91fb-c8468afcf920 | -10.1405 | -50.2913 | 2026-09-01 00:24:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 151f7a84-98d9-3f3f-8c01-a8364db0bd88 | -9.94553 | -53.99697 | 2026-09-01 00:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| fe1273ad-e3d7-360e-8141-b683f2cabc59 | -18.50178 | -50.89539 | 2026-09-01 00:24:00 | TERRA_M-M | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 905d9c5d-7e22-3710-b088-18a9aa907bd6 | -14.26006 | -52.88233 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5a9e109b-22e5-3de7-8d54-a82cd68682db | -14.26634 | -52.86248 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5660b794-8a54-3a73-9cbf-742bdbbf1832 | -14.41784 | -52.50171 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4804fdb4-7ac6-3792-85df-1a5d71b3aa89 | -11.69025 | -54.54561 | 2026-09-01 00:24:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8808cd5e-4529-3b43-a2ca-41e82bc21747 | -14.72652 | -53.57991 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a839289b-f129-37fa-888a-d85bd742d9a2 | -13.47924 | -57.06655 | 2026-09-01 00:24:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 75dd1309-e14b-33ef-9597-4c6b10fa1267 | -15.40117 | -52.73203 | 2026-09-01 00:24:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1c9765a9-d0cf-33a8-bb92-b9d70fbeaf67 | -16.44541 | -51.40622 | 2026-09-01 00:24:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 46424c5f-d92b-3667-8427-c68eac6b3261 | -14.46186 | -53.32626 | 2026-09-01 00:24:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8371afab-a770-33c7-92c5-fe0f4ca23123 | -15.24132 | -53.84262 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| db42c024-4b9a-325c-9f03-fb99207d4c19 | -15.56204 | -56.26811 | 2026-09-01 00:24:00 | TERRA_M-M | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8c327ede-5110-3a46-bb6b-54440c421204 | -15.83767 | -47.68204 | 2026-09-01 00:24:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b1d26716-a267-398d-bf61-91f5efc38514 | -15.76779 | -56.10019 | 2026-09-01 00:24:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 89eaa334-38b0-3f64-8580-1fb819bda0cd | -11.24678 | -54.00554 | 2026-09-01 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fbd8479a-f38b-34a5-bc83-9d4cbe9eaef6 | -19.18976 | -57.35617 | 2026-09-01 00:24:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 34048161-f37e-3d81-845a-7315ce9a72ac | -15.76645 | -56.08948 | 2026-09-01 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| a376166a-472b-34a1-aff9-997fc5480a37 | -15.24257 | -53.8517 | 2026-09-01 00:24:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c0582091-fc87-33f2-aa60-7088e75e5281 | -15.6537 | -50.09927 | 2026-09-01 00:24:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| b0b26383-575e-386f-993c-a4b52c8ee9be | -11.66073 | -47.6078 | 2026-09-01 00:24:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1431db65-a34e-3584-a90d-c424678354b0 | -15.6447 | -50.10698 | 2026-09-01 00:24:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 32.6 |


[Clique aqui para ver as próximas entradas](README7.md)
