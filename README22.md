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
| 3e5988fd-92cb-3377-b271-e3ee69593cb0 | -21.77577 | -56.30404 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6586cee-09a7-38f8-9987-4abacc51719b | -21.80725 | -52.71646 | 2026-07-08 05:16:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a0e6956-84d8-3f88-80ad-80a251ac6e57 | -21.79651 | -56.2653 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0b8fb1fd-72f3-3558-add2-3275f37012f6 | -21.80858 | -52.71606 | 2026-07-08 05:16:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a17881e6-997a-313c-8efd-306cd99020c6 | -21.77708 | -56.29385 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3914f996-6687-3101-8650-6a4def3e4b25 | -21.8121 | -52.71705 | 2026-07-08 05:16:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| acdbc012-2474-3cff-b34f-159cbb5b5b9b | -21.77191 | -56.30354 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58de96ba-f552-3fe1-b94b-558c042032a0 | -21.79972 | -56.27095 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f70d7d2d-e9c3-369d-9f04-2951838bb0ad | -21.79584 | -56.27045 | 2026-07-08 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6d9d79cc-22af-3dbc-beed-7763d52f8c52 | -21.8033 | -56.2729 | 2026-07-08 05:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c9c567b0-dd4d-315d-b775-097996d1dd50 | -12.7548 | -44.5428 | 2026-07-08 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 93d7ad24-6ff0-3f30-b5d1-31b85c44938c | -12.7553 | -44.5194 | 2026-07-08 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 08a7938b-67f3-3129-ab65-bb1cc4b5b7aa | -9.2258 | -48.5782 | 2026-07-08 05:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 8f6bf022-b848-3ad7-a2b8-111d46cb277f | -12.7746 | -44.5162 | 2026-07-08 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 5fd4a792-9e4a-37a0-a4f1-cd3c0b487c1a | -12.7741 | -44.5396 | 2026-07-08 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 06f2e399-e554-3a44-9713-7980ebb642d3 | -12.7741 | -44.5396 | 2026-07-08 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| bce82c9a-3369-3e38-92a2-2c910c82439d | -12.7548 | -44.5428 | 2026-07-08 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2611dbe4-1f5c-32ba-9b46-d5a1a63f4584 | -21.8033 | -56.2729 | 2026-07-08 05:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 92c453de-0c2c-38f8-a1c9-cd5d62695a74 | -12.7553 | -44.5194 | 2026-07-08 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 4d96e0e9-59d6-3e54-9bd4-16b9d9e6b83e | -12.7746 | -44.5162 | 2026-07-08 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a24a5a66-0df9-308b-b74a-92debe76c0f7 | -12.7741 | -44.5396 | 2026-07-08 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 87b06d55-41ea-3a75-992e-0027693d59c9 | -12.7746 | -44.5162 | 2026-07-08 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 954518b7-9785-3332-a731-4feac6b9a4a6 | -21.8033 | -56.2729 | 2026-07-08 05:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 51664396-3a7d-3c81-8c3c-a9482f7f120a | -12.7548 | -44.5428 | 2026-07-08 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bdd4555e-e5d2-32cc-bfd8-7b53f06faed8 | -12.7553 | -44.5194 | 2026-07-08 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 8173186f-8d98-3ee5-b9ae-04ef507d37e6 | -1.82505 | -54.48288 | 2026-07-08 05:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b85a4ac-8854-3abc-aebf-c1e3ec4be72a | -1.82814 | -54.48087 | 2026-07-08 05:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aafabd19-3c5a-3da9-924e-c4db88183715 | -1.82552 | -54.47989 | 2026-07-08 05:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b8e936f-2e22-314d-beff-3e6d4f9b379f | -1.82303 | -54.48009 | 2026-07-08 05:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c687e623-6c41-36c6-bda6-21bec5cf097a | -6.42804 | -55.80298 | 2026-07-08 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e31ca907-6db3-35ae-8747-f5a8dd4bb304 | -6.42887 | -55.79725 | 2026-07-08 05:46:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8bdaa9e-d139-3f96-9db5-6256968bcbda | -9.30625 | -51.9189 | 2026-07-08 05:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 37b1454b-efba-3377-bd42-af99de201770 | -10.25291 | -59.03027 | 2026-07-08 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a1aa7bc-8373-3ca0-affb-f8b5b0d5b77c | -14.14693 | -52.89223 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| feeb61f8-4b7c-3066-9af6-884956785522 | -11.90849 | -55.91059 | 2026-07-08 05:48:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10936622-4403-33af-9c2d-d6cdd1029d7c | -13.2884 | -54.40842 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5304f141-5a84-39d4-ae8e-4afbce00c741 | -13.28289 | -54.40314 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1921b44a-8bed-3b24-9457-5685bb3a0162 | -13.33586 | -54.38341 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e4c12e-b060-38b9-b93e-1e22204119f0 | -13.27531 | -54.41575 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c082f64f-371e-3e08-8603-4d81d6c46dcf | -13.53977 | -52.94522 | 2026-07-08 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bd1bee62-d370-33a7-9cb3-aedc42dcac0c | -13.335 | -54.37729 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5403441-0911-3e94-ab0f-337841258158 | -13.3005 | -54.40969 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8f4cd03-e675-329c-bd50-5b69b1d18ade | -13.33394 | -54.38618 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ba28424-af06-3752-8fd9-fec9eebda238 | -14.14341 | -52.8921 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fe84a800-f5ed-3db5-b682-e40613ade4ea | -13.28186 | -54.41204 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 377ce0ab-c227-3f6f-bb48-ccca2bb76f8b | -13.29393 | -54.41354 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cdca807-1ae1-3e2f-b9e3-02d7571a6e0c | -13.28892 | -54.40398 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 863ad315-1d87-3bff-a664-d2befd4bb86e | -9.50374 | -58.38268 | 2026-07-08 05:48:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7eee6f7a-2ebd-358d-a556-b5c955d6447e | -13.29497 | -54.40465 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b2f75c6-8c64-3fb0-94de-c698d34a6144 | -13.3298 | -54.38269 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 391b08bc-7d76-3e65-a5a1-5f16b8c5bbb5 | -13.32789 | -54.3855 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1ecfd42-8d57-38a0-9274-5a65db2d5b70 | -13.29341 | -54.41798 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9526e177-1cc6-328f-be8d-9a83c811b5fc | -13.28135 | -54.41645 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f5a6ae4-c9f1-3e69-9960-a09acf0cd1b3 | -9.94639 | -65.0156 | 2026-07-08 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e55d9a3-3f47-3837-9195-81d6dff221a4 | -13.29445 | -54.40911 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c9dec3-33ab-3d2f-8819-e9f49cf12fc8 | -13.33536 | -54.38791 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e22da7aa-338f-3fd9-a38d-eec7b08c663b | -13.33636 | -54.37895 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbd4cdd-882c-3069-9a20-e23fa89a62ea | -13.34106 | -54.37796 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02956f54-1f2d-34a6-b72d-9e2b9b999084 | -13.53318 | -52.94414 | 2026-07-08 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 867fed46-878f-350c-91a5-3f524137b716 | -14.14408 | -52.88605 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 785a0eac-b37e-3a9b-826f-67d73cc2c988 | -14.14756 | -52.88624 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1dd8e29d-3964-3f1a-bfd5-ed624fa6776a | -10.25715 | -59.03092 | 2026-07-08 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5389835-427c-3799-9bd4-db80d2a5d218 | -13.28789 | -54.41286 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5becb997-dec7-3fae-8fd7-c82d0bb338fc | -13.3293 | -54.38717 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56917b4a-f651-36da-831f-85404038cb48 | -13.28238 | -54.4076 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61d0794a-7ceb-3b6f-b4a6-be7bbb5d014c | -13.33447 | -54.38174 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e92b37c9-d68e-3ae0-b44a-4ae6edb12630 | -13.33031 | -54.37822 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7657867-4dfa-3dfd-b326-ee5ac4924ea9 | -13.34242 | -54.37962 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36ad7a02-922a-3237-aa67-29fb87ddc2d2 | -13.54042 | -52.93922 | 2026-07-08 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9aef8999-315b-39e8-8620-103925749db4 | -8.66778 | -63.86055 | 2026-07-08 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5c02675e-ee71-33bd-8e71-761a2ff6a2ea | -13.32841 | -54.38104 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 273735cc-8d12-33ac-a297-8babfca1d9e0 | -14.14086 | -52.8855 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4dd963f-6a12-38f3-b7f9-5613c6bc5544 | -9.77816 | -63.50326 | 2026-07-08 05:48:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37c92555-d1cd-3af1-a60a-1fdb36c24eee | -14.14023 | -52.89158 | 2026-07-08 05:48:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c969608-6ac1-3fbd-912f-09ebbba6e835 | -13.27582 | -54.4113 | 2026-07-08 05:48:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33892b93-fd8c-3bf1-a808-96fa60ae8362 | -12.7746 | -44.5162 | 2026-07-08 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| d21ed231-8a9a-3e2f-967e-fbb5ee55c35f | -12.7553 | -44.5194 | 2026-07-08 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 6132116f-ca54-3cbc-9a87-81b61a331f80 | -12.7548 | -44.5428 | 2026-07-08 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ac5c6301-4998-37d7-a269-e9709b9e3900 | -12.7741 | -44.5396 | 2026-07-08 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 6771f248-c101-3eaf-abd7-8bb26e881609 | -21.8033 | -56.2729 | 2026-07-08 05:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 49.0 |
| a2bbfda1-2d1e-3f6d-b9dd-26ecfaedd61d | -21.8134 | -52.72017 | 2026-07-08 05:50:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a26659a4-9fdf-3f38-ab9b-022839805c90 | -17.53489 | -54.01178 | 2026-07-08 05:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6466c3f0-ae7d-31a4-ad5f-cb75826365d1 | -21.79626 | -56.27718 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6f507c3f-86a8-3594-bec4-183c541cc346 | -21.77685 | -56.29363 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12bbb61e-42f2-37a5-8950-eb702b69796e | -21.79704 | -56.26842 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd8de8ff-fb0f-3d24-8758-57e4391c6125 | -21.79744 | -56.26389 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64db3512-102b-306b-9ab6-15e15f8ac214 | -21.8061 | -52.71972 | 2026-07-08 05:50:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40c8caae-92cb-3fc4-b276-d66c3f9583ad | -21.77201 | -56.30505 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f7029ce-437a-32c8-8a2c-eb714f95617c | -21.77286 | -56.29609 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3462fd2-df04-321c-bb71-645db7116509 | -21.80261 | -56.27318 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cfa791b-1b10-3917-970f-c916c99d0943 | -17.54087 | -54.0178 | 2026-07-08 05:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20af4b21-2142-3aa6-87ab-f1cfa2d65e00 | -21.77607 | -56.30247 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2afa9886-3a0e-3171-bd07-95e85e2e5a72 | -17.53438 | -54.01711 | 2026-07-08 05:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b8935c6-55e9-37de-a4de-30375ca06d24 | -21.77646 | -56.29803 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd3532b9-1198-353d-a754-7feb559da724 | -21.76973 | -56.30653 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8dda2398-9ad2-3d03-8fa3-efc678b7f123 | -21.79665 | -56.27286 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f1365965-9789-31f9-862e-2da3a3b61bee | -21.80301 | -56.2687 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48383350-32fa-360c-9e9f-46120223a476 | -17.54141 | -54.01293 | 2026-07-08 05:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 690355dc-f5b2-3417-ad1e-72b5ffc9e1cf | -21.77567 | -56.30696 | 2026-07-08 05:50:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ac82995-5bea-3ef0-8601-b94de3866b5a | -17.54139 | -54.01252 | 2026-07-08 05:50:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
