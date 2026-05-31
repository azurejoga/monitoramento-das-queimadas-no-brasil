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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 688ec615-b1c5-3b8b-8b09-958fa153204e | -10.07532 | -51.66187 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a7e05e50-8ee3-30bb-80f0-6b7ce7ae9f9f | -10.07069 | -51.65742 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a0d18a74-9f34-3313-b62a-fca2e6f9041f | -10.76173 | -46.91809 | 2026-05-31 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7aae86e-5837-34a6-99d3-d6b14589cf92 | -6.9892 | -42.88563 | 2026-05-31 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9c4e3cdf-f677-3eee-a1a9-e5806d083d21 | -10.06354 | -51.66636 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c80ee83f-6cff-308d-b76a-148f1f27561a | -10.07192 | -51.65087 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ef6bd55-9952-323e-b0da-340b5a043816 | -10.0747 | -51.66517 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 17e13510-b3b2-305d-b2f0-a2683bf2de16 | -10.07345 | -51.67179 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bf4740ec-012b-3714-94c3-4ceccf6f8332 | -5.52124 | -37.48703 | 2026-05-31 04:17:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 44394bba-3f73-3224-ad20-3ada5de0a073 | -5.51994 | -37.62333 | 2026-05-31 04:17:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f9936cc7-9d6d-38bf-9628-7824bd4f2bf6 | -11.6233 | -55.17141 | 2026-05-31 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd29b550-1992-308b-a567-ae94d3ea4e31 | -6.99256 | -42.88618 | 2026-05-31 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a8389494-5661-34e5-abfc-02466842a802 | -10.14298 | -48.0804 | 2026-05-31 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d38bdd0-cee1-3ee1-b5ed-40f62a961439 | -10.14429 | -48.081 | 2026-05-31 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 986da818-f139-3632-8f78-5476495b2298 | -10.51762 | -42.37164 | 2026-05-31 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4c726563-0cca-3f36-a0c4-10fd668f3c1e | -6.99313 | -42.88263 | 2026-05-31 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3f1f69ec-c320-3e6a-b015-e1fea88e9e84 | -12.12222 | -47.21733 | 2026-05-31 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae38335b-769b-3d00-bbd6-c8b75ae5f82d | -10.0648 | -51.65971 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c6784909-4e3b-3fdc-a240-8d4e3620a8d1 | -10.05763 | -51.66869 | 2026-05-31 04:17:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1c491dbe-7459-3ae7-99b2-3b33ce466f37 | -9.48952 | -48.66363 | 2026-05-31 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34e197a9-c837-3e90-b8bc-b06b71555180 | -8.20616 | -49.83927 | 2026-05-31 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d79bc94-50e2-3b90-b449-9dd03110a0f1 | -8.25905 | -48.23209 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b83c1e8f-df4b-3390-9de7-e7048ad808d0 | -7.50793 | -55.01178 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8539330-4bb3-3184-92c0-ae674455b84b | -9.16374 | -46.84078 | 2026-05-31 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac20eb0-c623-38af-8eb1-012bb8a13313 | -8.25835 | -48.23622 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0b2be8a-8542-3b6f-bffb-46241e77e32f | -8.04156 | -46.5837 | 2026-05-31 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8529920b-6353-3040-9a99-c55dfe12fc24 | -21.40184 | -45.49272 | 2026-05-31 04:19:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f704e19-ca94-3c83-9291-1ca36182efe2 | -19.17212 | -47.35397 | 2026-05-31 04:19:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841bf6a1-7a30-3927-b9db-d4ccaf1d2eae | -14.7686 | -52.6734 | 2026-05-31 04:19:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 708b319c-9976-341c-9064-b0b4e6fa9eb0 | -14.76797 | -52.6766 | 2026-05-31 04:19:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3605ee0f-bc85-3077-bdf1-2853fcd0ea31 | -7.63937 | -47.30227 | 2026-05-31 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 649f0e42-6399-3d51-b0ef-d3ffbbdfe5c6 | -8.0424 | -46.57878 | 2026-05-31 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eae50744-0b2b-3f6d-b597-e7b483b612a5 | -18.36839 | -47.57893 | 2026-05-31 04:19:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bb8793f-5854-3d95-934c-2ed602e9a843 | -9.16042 | -46.83828 | 2026-05-31 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 767aae6d-9b53-361b-adb4-548617ce43e6 | -9.15984 | -46.84008 | 2026-05-31 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b59506e-71b8-3dfc-bca3-50eced5d5f6a | -15.86773 | -52.26928 | 2026-05-31 04:19:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e468650-1646-3096-ad57-bcd151f0715f | -13.78831 | -53.40437 | 2026-05-31 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b40dce-092a-3e74-b512-ca3ed4ee61d3 | -8.72969 | -48.32217 | 2026-05-31 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9920a7b2-7ba8-3d35-b84e-20f30d81a699 | -7.63875 | -47.30597 | 2026-05-31 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8987b52a-a148-34cd-b15f-e73590251a98 | -21.40243 | -45.48901 | 2026-05-31 04:19:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5ab0cc40-ba5b-3b16-8c33-867a1f4c416d | -8.20393 | -49.83992 | 2026-05-31 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff6bf41b-8b5f-3b1f-b0f5-b21d20d50c07 | -8.12056 | -46.47158 | 2026-05-31 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3eed2bc8-1bb3-39c6-960d-9a8ebaf77aca | -13.70791 | -52.97855 | 2026-05-31 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dbca4e50-e13c-3775-83be-f5580b67fc47 | -18.48905 | -46.88855 | 2026-05-31 04:19:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42964e03-6030-3444-bcff-72206aee376b | -13.70325 | -52.97381 | 2026-05-31 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec7c7052-1d6a-382e-b5fd-c630cc464972 | -8.12246 | -49.5596 | 2026-05-31 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5fbb82c-8492-3c35-8b3a-c29f63443258 | -7.50144 | -55.00495 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c05f4cc3-e6da-375d-bef8-29d4c52109e6 | -7.4955 | -55.0034 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fefd02f9-04d5-3e75-ac65-8be46060d02c | -9.41573 | -40.37035 | 2026-05-31 04:19:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aec9817e-c060-3717-9b2a-3ca3737c8802 | -7.50034 | -55.0109 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb2f4a70-50b5-3f5b-b2e6-57486edbc983 | -9.15652 | -46.83759 | 2026-05-31 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 426f1123-bcc4-3e3b-82f1-42b04677bad4 | -19.17563 | -47.35469 | 2026-05-31 04:19:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccf418df-5db4-3b25-a9dd-b17baf0e2418 | -19.86657 | -43.87095 | 2026-05-31 04:19:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 119b3076-04c5-39bf-80fa-1a2c576bff83 | -8.26196 | -48.24115 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f4c9e0-51d7-3301-a67f-43886b34480d | -13.78618 | -53.40646 | 2026-05-31 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d745c144-6637-3dfc-8874-7c878726dd14 | -21.25652 | -47.8261 | 2026-05-31 04:19:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 707f2f93-eabc-3a11-a31b-fe750309db21 | -8.73329 | -48.327 | 2026-05-31 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ada989-cd08-3172-b9ab-f8b122168ac9 | -8.26338 | -48.23288 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b22e719-9de4-3bcf-ac3b-c24df64756ca | -9.1635 | -46.84388 | 2026-05-31 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cbce4e0-4140-3dd5-94bc-a68e4ed0d5c5 | -8.26649 | -43.93059 | 2026-05-31 04:19:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f15046ac-91ee-3e84-a092-2610d5642a9d | -8.72898 | -48.32623 | 2026-05-31 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9afd382-d1d6-3c40-a3ad-04dfb76cae82 | -8.26268 | -48.23698 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c65081-ace3-3f9e-a66b-f70e4a7f8eab | -8.20522 | -49.84464 | 2026-05-31 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81c0a4d9-045e-39a3-a5e9-2c77ec5a9547 | -8.25473 | -48.23132 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82986a1d-7672-385c-8e93-9d62c101741d | -8.25402 | -48.23545 | 2026-05-31 04:19:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d8b24f9-524c-37a6-a5b7-7ad3021539b1 | -12.8054 | -54.86984 | 2026-05-31 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0834f3f2-6963-3a2c-a5e5-c0e6c544f12b | -7.50225 | -55.00478 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02d1fb71-fd85-3b85-80cd-495c687b4153 | -13.70254 | -52.97738 | 2026-05-31 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 420f965b-5fa6-3f85-9064-baaa8e64fb11 | -13.78757 | -53.40807 | 2026-05-31 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11908730-300e-3897-9091-32393060e848 | -8.20875 | -49.84081 | 2026-05-31 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47dc5a20-a439-3783-a9f3-d28a2ee1c84e | -7.5011 | -55.01077 | 2026-05-31 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 235d8191-15ed-3178-93ad-5df2777de441 | -13.70183 | -52.98095 | 2026-05-31 04:19:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38544d62-048d-3424-b827-bd6b1a54a7b1 | -10.0725 | -51.6559 | 2026-05-31 04:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| f373c2ea-fbfe-3c13-aaa0-e0ee3b954b57 | -10.0534 | -51.6786 | 2026-05-31 04:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 71e4d96f-f673-3b6a-b088-7539645ce3f7 | -10.0723 | -51.6769 | 2026-05-31 04:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 79252694-2bf1-3012-8899-7b331626637d | -10.0537 | -51.6576 | 2026-05-31 04:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 825c6496-c416-317c-8bf8-817f98b4c6f4 | -21.32768 | -47.771 | 2026-05-31 04:21:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| effa4716-2393-34ac-a07c-1b79fb38ddaf | -21.80567 | -49.12772 | 2026-05-31 04:21:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d9dcec0b-a75e-3977-84e0-8e7751693840 | -23.14979 | -51.66048 | 2026-05-31 04:21:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8902960c-fae0-3b3f-8fac-32e28502a957 | -21.80935 | -49.1285 | 2026-05-31 04:21:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8dac6bd6-0abc-3067-afc3-122169e72803 | -21.49088 | -48.38178 | 2026-05-31 04:21:00 | NPP-375D | SANTA ERNESTINA | SÃO PAULO | Brasil | 3546504 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7af1021-2540-3a54-9307-56a961f96a3e | -21.32418 | -47.77033 | 2026-05-31 04:21:00 | NPP-375D | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 057a7bd2-6a80-3412-92e5-07cf0fa86789 | -28.05866 | -48.66819 | 2026-05-31 04:21:00 | NPP-375D | GAROPABA | SANTA CATARINA | Brasil | 4205704 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 04c282e3-4e6d-3ddb-9f92-9e0860734b63 | -25.72428 | -53.7484 | 2026-05-31 04:21:00 | NPP-375D | PLANALTO | PARANÁ | Brasil | 4119806 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 28f31c91-5b8b-3bd2-9c00-d372387f42dc | -23.15078 | -51.65955 | 2026-05-31 04:21:00 | NPP-375D | ASTORGA | PARANÁ | Brasil | 4102109 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 26d15c89-e21b-3002-8d90-0da46e2cf4ba | -21.2145 | -48.54498 | 2026-05-31 04:21:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b60902c3-4a20-3030-a976-bd302964403b | -10.0537 | -51.6576 | 2026-05-31 04:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4483f212-9961-39b6-a424-7f46e6fd75ab | -10.0725 | -51.6559 | 2026-05-31 04:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| c2866a94-35d0-3dd7-b283-764380548b49 | -10.0723 | -51.6769 | 2026-05-31 04:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 171e3523-5ca1-31a8-a089-952976855e70 | -5.52203 | -37.48762 | 2026-05-31 04:34:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3853b758-400e-354c-8ba6-1a5da9d3b111 | -5.613 | -37.52953 | 2026-05-31 04:34:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48238eb5-1ec3-3817-a8ed-c210d9d61cf5 | -5.52261 | -37.48364 | 2026-05-31 04:34:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8aef4009-9807-3713-bd3e-3a5987b6a737 | -10.7486 | -46.92096 | 2026-05-31 04:36:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bae7631d-9473-3f14-b259-da1bff893862 | -6.04607 | -47.89262 | 2026-05-31 04:36:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 803e1fb6-4011-38ef-8990-a9cadf0e35b5 | -7.2226 | -47.19292 | 2026-05-31 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24716b14-1119-3eda-8b51-545f12391108 | -10.06491 | -51.66511 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 02063c4a-23e9-368d-9cc9-336baca3e4b9 | -10.0619 | -51.67023 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 333a5805-d106-3989-9553-bc3ee011a9ef | -10.05833 | -51.66963 | 2026-05-31 04:36:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d3e0e089-da0b-3401-a678-45a70365ac0e | -6.84062 | -47.93701 | 2026-05-31 04:36:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b0ab788-cf10-3a13-866c-fb2d7d4c720c | -10.81039 | -49.3374 | 2026-05-31 04:36:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
