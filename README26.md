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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64969531-2c24-35cd-ba1a-9100c0568045 | -8.44286 | -43.85712 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8d30dc4a-131d-348a-b44e-dc93e6206f59 | -10.29791 | -50.27306 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2d7fd8c9-5c22-3042-acd0-337c963944d1 | -10.30574 | -50.27352 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 91facd5f-1abd-3419-b1b5-66d93be841d7 | -8.16303 | -54.76496 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3099ec40-6aed-3136-a46c-9cce164c8e9d | -11.32694 | -47.28601 | 2026-09-20 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9dc3a5a-c4f6-3c95-9f3e-336a27d9df6b | -8.04999 | -46.28959 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77560c30-251e-3bf3-b0b1-563ccc7fe13a | -10.13303 | -45.55751 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc09eb3d-5bc4-32bc-8a49-874c4de187b8 | -8.664 | -45.43516 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be0f8978-cb67-3111-b3ac-8a0e758d5a3c | -11.449 | -45.33022 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d864527b-28b9-3919-94e2-647648df38f2 | -7.182 | -47.90042 | 2026-09-20 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e122befb-9dc6-3b62-9f89-2b21175f7a5c | -10.3135 | -50.23035 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4d9c8d8-efdc-3795-9d16-ae87e2518b32 | -8.43127 | -46.86051 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7925bf3-51e7-30c6-9834-2c06ef3d84e6 | -9.79424 | -45.05689 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f018308-1f18-369a-9dcf-ab243b6cd052 | -8.16761 | -54.76576 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3471de78-c440-3b6a-a4bb-3976e4b1f2a7 | -5.65301 | -43.37258 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3f8f2cc-f225-3374-a9a5-34cb9d5ddf9c | -9.60799 | -45.39415 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91dc8cb0-1bb0-3609-9cb9-4a6ba834aaca | -8.66767 | -45.43578 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f8bc29f-8869-38a9-8222-f4fc791b0e36 | -7.43284 | -44.75275 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f1097b8-ae23-3ea1-88ae-54569ab0983d | -8.05186 | -46.25486 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 18b9531f-36e8-33bf-90fc-28e0f5464a9c | -5.83903 | -53.5327 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5882295a-5848-35ff-9161-b9bd83dbab8e | -9.69416 | -48.31804 | 2026-09-20 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4fd0d43-3e85-3571-a209-f3adcb6065ea | -7.68648 | -44.66187 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ab4d0ea-b112-3d33-aafc-335e5d5c6391 | -8.61055 | -54.60632 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f116fc33-fab7-3f36-a362-cb6dc1df4056 | -11.48318 | -45.36507 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f89e9101-d123-349c-8062-ee0c08b49a16 | -9.70686 | -45.86868 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c3a5b58-c1b8-3e50-8f57-cf5c608e1b81 | -5.22983 | -47.58412 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2af33485-88d4-3f3e-8014-14ef573e17f9 | -6.60053 | -45.52792 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e74397ca-3645-3549-8ec6-458667ab73fc | -3.74431 | -51.81653 | 2026-09-20 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53b25eef-1991-3495-89a9-b6f600b8b2c4 | -8.16205 | -54.75853 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aec2af7f-8d9e-3785-b97e-603d017f48b7 | -10.30096 | -50.25688 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc4e547-04c3-34da-9ae0-6c26803346e2 | -8.07794 | -55.34785 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c0024539-a9db-3b9a-96c3-c5aa88703775 | -6.92482 | -42.90493 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac2d02a3-a8e0-3e69-be37-7dcd3cf4af64 | -7.62671 | -45.4284 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65f3e695-cfe8-3042-a588-f5bfed715172 | -7.54758 | -45.38956 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff654ddc-d13f-31dd-9b84-e478ee2de353 | -11.46301 | -45.39871 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49cd0495-dead-3f75-aadb-0263082bd8d3 | -4.72571 | -46.12856 | 2026-09-20 04:19:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53ad9651-4854-3d6a-b436-a26da8ca7da5 | -10.25641 | -45.42407 | 2026-09-20 04:19:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b91498a6-2017-3bb5-8049-aae49297a1cc | -11.02033 | -48.28887 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a5bf22a-e37d-3ecb-abcc-bda95eca7423 | -7.43644 | -44.7533 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e715302b-0802-3809-883b-883ea220f584 | -8.66929 | -45.33482 | 2026-09-20 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6500415e-26eb-3897-abc0-5a8791490f5c | -5.31422 | -45.25045 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f818551f-bef6-3b61-adf7-0b2b5ff2e5bf | -11.48539 | -47.75953 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88deb252-5ce0-3d05-b59e-570e737a8ffc | -9.12757 | -45.72033 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a35478e-9db6-3a49-96ef-0c81d87c9821 | -5.85682 | -53.50626 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa74b1e9-72a3-3454-9385-323ed29061ad | -9.56625 | -45.46502 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fad3ee86-b7db-36dc-b3d9-7f35d0ef58d8 | -10.5468 | -46.74382 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b12b323a-b8fe-3f31-b478-a40c7dc1854c | -7.10968 | -43.07831 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc54f326-b9e8-3bc4-a018-d6c892ca9612 | -10.29896 | -50.25544 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acf5229d-b4b9-340d-9482-1cc0764abf20 | -6.29612 | -47.60763 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3123fe95-1df1-39ef-a6c4-eee94fb62101 | -8.17208 | -54.74227 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8b2a077-857c-32ea-a7fb-491257407ea3 | -11.43702 | -45.42329 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bb890cf-8240-3e6d-9bf9-087a0c66a870 | -10.30769 | -50.2348 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea2c7414-a6d4-3b54-b3bb-a565b17f2922 | -7.54465 | -45.43011 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 00ae62be-6c9b-31e8-9221-4c009a30e8b0 | -6.87962 | -43.07196 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b1549aa-f1b5-39f0-aa22-c606b69264ae | -8.63162 | -47.62387 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 495042a0-17a3-3076-bc54-e54db48ca726 | -10.12642 | -45.55253 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e1b7349-8e64-3957-b1ed-842116132a8a | -11.14965 | -42.79667 | 2026-09-20 04:19:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e8b02b83-01fd-3d8a-b3db-9ec7a28fc4d0 | -3.95333 | -49.0433 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7f832e3-576b-345f-a87b-d91f894928cd | -5.66709 | -45.30964 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29e0aaec-eec1-3262-8b8a-93a3b2d0b385 | -8.21832 | -45.61367 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfcc7d73-287e-33b7-9b34-06418d0868a6 | -5.84098 | -53.51972 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c618cf0f-810b-3588-94e1-02d120f96feb | -11.03231 | -48.29468 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4edeab76-5e9d-3cf3-b1a6-45a4ec361133 | -6.47684 | -43.91585 | 2026-09-20 04:19:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9cbeac7-c607-3766-8acf-a07e55d9a14e | -9.92586 | -48.38077 | 2026-09-20 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b3bc7da-7bb3-3e87-b552-e340e5d78a1d | -11.8042 | -46.85372 | 2026-09-20 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bbb97b5-55a6-362a-ae6a-fd125661bcaf | -6.16779 | -47.49438 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 161a6149-0f0b-347a-8250-b2d36298dccf | -8.36038 | -47.24936 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b0a829d-a03a-35f6-8912-70692de8480c | -6.61211 | -43.7525 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff6f2e15-674a-3972-ae34-bc6d05983483 | -8.65523 | -45.44263 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a9927f4-fc14-36b7-be08-f02a7cd723b7 | -3.46187 | -50.61271 | 2026-09-20 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b78beee-b0fc-3cd5-855e-b5fe20e93881 | -9.26493 | -46.19175 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52db22b6-7072-3cf5-8fd6-a48896e0e678 | -6.30687 | -41.76305 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 558b162a-d988-3190-8be9-675c6980d394 | -7.59111 | -46.34991 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55306187-99fa-33eb-9eef-8df6f05c9a47 | -7.55289 | -45.44962 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f291dfe-b0ac-3ce1-a166-226224ac4120 | -9.12312 | -45.72418 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17bb1a6f-ad0e-38b4-8b70-29b079044279 | -8.50531 | -47.42715 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f85cc413-495e-3713-b72d-f6238813adef | -4.98269 | -45.15068 | 2026-09-20 04:19:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf016d01-4ba8-39a8-aaef-64f52350b711 | -6.98795 | -43.37348 | 2026-09-20 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2726414b-dc16-3b68-a6ca-e5ce48bb17b3 | -11.02317 | -48.29726 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a630d27a-c915-3d17-a3a2-d7106a31e0b4 | -11.48941 | -47.76032 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e97f63f-9290-3bd5-bccd-5a2d8685d2bb | -10.60343 | -46.52895 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0db59ed7-738a-37ae-aea3-73d73292f782 | -5.83898 | -53.53043 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 493df246-1188-357a-a274-c7ad04f0c37b | -9.28418 | -44.38824 | 2026-09-20 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d78aa6f-9681-3c56-a1fb-4a27fbb5073c | -8.72858 | -45.44958 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f560da25-2821-31ea-9413-f85e4b648cd3 | -5.79071 | -51.86527 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d73705c8-0e54-3439-9715-d7ef9c14a835 | -9.81559 | -46.39077 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ae950d7-3751-3670-9d51-ef336cd62f72 | -10.31931 | -50.22589 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ebee2b8f-5931-39d3-bd40-0d9a4e2e1eae | -9.83655 | -46.444 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa1bcd0d-57bf-3863-b231-aad66a0f7eca | -9.9737 | -46.5733 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19de6d8f-e8df-3899-8cd4-2d17d22d1d38 | -10.29603 | -50.27165 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 68395477-26f1-3f8c-91b3-8a5ce45861bc | -5.40505 | -44.28552 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d8768a4-a397-3551-9a7b-8d12ab20d816 | -7.54207 | -48.68286 | 2026-09-20 04:19:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6269372e-24b2-3630-abf8-1a6bc7e18af1 | -10.07642 | -45.67169 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e6a296d-7ed3-3db9-9f11-ed09a29be205 | -11.03162 | -48.29855 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7be01b0f-4828-303e-b7c9-e38dddc35760 | -8.6116 | -54.60081 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34ba85c3-851d-37f9-9034-f2ded35da507 | -5.85197 | -53.53489 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08151318-f78f-3069-96f0-1eca5c84e2a4 | -7.41877 | -44.70404 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1321816b-66f5-360c-b8ff-f32831e56a19 | -9.73014 | -46.09346 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc3a5fe7-2b2b-36c9-a1db-bdf33bdd8ba9 | -7.58345 | -46.73592 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72d180ff-9ec5-36c7-a263-fc370db62ef3 | -11.44056 | -45.4239 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
