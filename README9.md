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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a50d75-a4bd-3b66-b5d5-340d5f590ce6 | -9.32985 | -44.83574 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2425cd2e-9ec2-32f4-9ffa-af445e3b81d7 | -10.47747 | -49.1443 | 2025-05-17 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d208f089-cf36-39a4-a87f-28ab7d992e4d | -11.64532 | -48.03153 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b9c8827-5aa3-3b05-97c9-079eb4d7f622 | -11.72192 | -47.73424 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d70c09d4-e568-3377-89d5-e055cac33b43 | -12.83747 | -47.40764 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ba0659-3cc9-3b2f-ad51-870ef9e68f1f | -11.57687 | -47.61299 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 17afe943-26ba-3634-9a1d-36ebbe443b57 | -12.10615 | -44.74506 | 2025-05-17 04:38:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bdfb529-9909-33fd-a3f3-ab1b67aae319 | -11.79714 | -47.40776 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb3ade19-1189-3559-94a9-53b4ce97770d | -11.27703 | -52.47008 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fccd4a87-d49d-3861-999f-90ee4ad65f7b | -7.90245 | -44.48677 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8332aa04-29a7-342e-82d9-c98e70d0840e | -11.35481 | -52.96046 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58141f31-5ecb-3f3d-b12f-34e889db8624 | -11.78996 | -47.39925 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3881f3a9-6c98-34d5-a674-b30e8651889a | -6.72344 | -42.13066 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| c35b04f7-02c9-3ad8-94e6-36426905bd6e | -11.41738 | -54.31925 | 2025-05-17 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b24ffc-7749-3d46-b3f9-8261129f85b2 | -13.31959 | -45.38842 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ac1bcca-9808-3f48-9253-fe4c67107509 | -9.41962 | -49.33985 | 2025-05-17 04:38:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e4aed31-b519-3cac-b265-14c7c917e0d8 | -10.47411 | -49.14376 | 2025-05-17 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1bd5f5e5-80c1-3da1-af84-a9abf754ce4d | -12.29388 | -52.47269 | 2025-05-17 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01517a94-2b84-39b9-bd57-4ea7ad8ede50 | -12.30068 | -52.47384 | 2025-05-17 04:38:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9680bd68-e185-3ff4-8c30-79a5405969c7 | -13.31178 | -45.38338 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b08f54c-8373-319b-a842-107853cf0cb2 | -7.22655 | -44.7111 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae11c61e-ad5b-39b2-8a86-d431baad5252 | -6.71822 | -42.12226 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b0c4bd3f-7a71-326d-b848-5d811b1eb691 | -10.27668 | -46.80099 | 2025-05-17 04:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de4a1e9b-74e0-3f54-bb39-277523060327 | -7.22706 | -44.70756 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8149185a-c144-300a-a4c1-ca2b3946daf1 | -6.62185 | -48.00678 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa169c4-7412-32b3-8bf6-aaa85da9a94e | -13.31802 | -45.40001 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26fbb73a-364a-322c-8472-f558216f382c | -7.90706 | -44.48007 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef121e03-e0a3-3b11-89f5-eedf1abbc85f | -12.35184 | -49.97265 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da143a1a-9a80-3353-bdcd-78b13eb64372 | -6.62749 | -48.01508 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a4f8f2-4769-38a2-a18b-1b07a1aa7302 | -11.35545 | -52.95655 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb3d0f96-9b43-3d00-bd48-39cee1a851ec | -12.83444 | -47.40269 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a67b8b36-9889-36e4-bf1d-bda7e6587824 | -6.78589 | -47.59781 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0da0c63b-984e-3480-b8e4-18d5628a6c50 | -10.02727 | -48.69695 | 2025-05-17 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d2629cb-c057-36ec-a0b9-199d2c87efae | -13.05739 | -47.82566 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a12f7109-92c0-3635-9d1f-4201a6936ba6 | -13.36162 | -43.08748 | 2025-05-17 04:38:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 447ae4e5-af7a-3e27-b9b7-8405fc9ad9b4 | -11.64122 | -48.03495 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ecac6cb-b0b7-360b-9022-8c8307244769 | -6.84125 | -42.79813 | 2025-05-17 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b101bd40-7325-3a36-92ff-bb01c3783bdd | -11.58282 | -47.62229 | 2025-05-17 04:38:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e054fcd-1782-3fdb-8ef4-a7290e0da7b3 | -6.17208 | -48.06308 | 2025-05-17 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9eb7a51d-2519-3c63-a268-5181b4eb5ff8 | -9.54632 | -47.66936 | 2025-05-17 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9115695e-717a-376a-88d2-915b07528ec5 | -13.32063 | -45.38064 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 992f19cb-78df-336c-8b3c-7af7d146daf5 | -11.39651 | -52.95504 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97fe3bbe-0790-32c9-907a-ce97f5ea7184 | -6.72693 | -42.12865 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7607b295-fed4-3d79-8a3b-96f4368b2d66 | -7.07667 | -44.91756 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68173f16-ba1e-36cd-9597-ce6053eb71e8 | -13.31386 | -45.39942 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 168c60c5-2eb8-3f3a-9bf2-c3c954bdf5bf | -7.80266 | -46.21538 | 2025-05-17 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a226f62f-7486-302b-8862-b09a75c1ae7d | -11.6383 | -48.03045 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f0a8b64-9cc6-3f8d-bf95-dcffb53a5481 | -13.30917 | -45.37118 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| beee1739-d609-34bf-9cbd-eb8c0a49a537 | -11.78634 | -47.39873 | 2025-05-17 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a386450-76af-3019-b0cc-b95cb67d61d8 | -13.31022 | -45.39495 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee5b54ec-ebb9-300c-b3d9-544ba30dae4d | -6.17264 | -48.05949 | 2025-05-17 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd01151c-ea97-3822-8b58-891a37f280d7 | -7.23403 | -44.71579 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 611bba9f-f9cf-3918-a89f-4aad26bb5cb0 | -9.79564 | -47.73815 | 2025-05-17 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed7d7d61-ad41-359c-aa5d-38dec66d4e08 | -6.78645 | -47.59408 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40326ff2-582c-388a-a2a6-87c81be5c038 | -9.25363 | -60.32204 | 2025-05-17 04:38:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26bdf343-5d74-3cd0-b01f-de9c1e8495db | -13.30761 | -45.38277 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba519ccd-3afc-3461-bf24-f59d78bd146c | -6.71803 | -42.13501 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 419de698-88ec-3cdf-b4af-05a358dfd883 | -9.30589 | -44.82854 | 2025-05-17 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c805c29d-de08-34f3-aa73-7c88ae273fe8 | -11.36306 | -52.95383 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d87f9393-b6b5-370a-9dd8-412d448825b1 | -7.90194 | -44.48674 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f75240e3-ff3c-3936-83cb-5adea2b2f1cc | -6.70258 | -42.13037 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7b74facd-e829-35b1-8ba9-2d68b576841b | -13.30448 | -45.37445 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dfc3fd8-8f96-3c3d-bf69-aee9320f4bb5 | -12.35016 | -49.96142 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c25b6de-68be-3395-9e57-922e847f93c2 | -13.05681 | -47.82967 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c61e5c9e-42f6-3ec9-9f3e-b2cfcd69fa0c | -13.06514 | -47.82291 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d2b2047-cf80-386c-9f60-2c9d48e588a5 | -13.04721 | -47.81976 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e1f14d6-e13b-3a8e-836a-80b4136a6e7a | -6.71675 | -42.13234 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bd13a47b-9c4a-39ee-ac62-983113d98062 | -12.11994 | -54.6629 | 2025-05-17 04:38:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1faa0f06-3a64-343a-a6f1-5a8cfd3b077b | -6.17083 | -48.05943 | 2025-05-17 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e835ca4d-f27b-373d-a1dd-8508d5a999e3 | -10.63376 | -48.08529 | 2025-05-17 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 162fc506-50d7-304b-8210-c46f28b5f4b0 | -11.96949 | -48.11058 | 2025-05-17 04:38:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6e78646-9291-343f-9855-afc6a50d453d | -6.16597 | -48.522 | 2025-05-17 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fef6335-7b23-3ea5-b52e-9b119e53c798 | -6.71685 | -47.59089 | 2025-05-17 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb882834-8d05-3dc2-814f-9c2cb5613517 | -11.16128 | -48.67206 | 2025-05-17 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc5caca3-c422-36fd-9043-9871e6ad75f3 | -11.6424 | -48.02702 | 2025-05-17 04:38:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae52cebd-cf98-3efd-8f48-ca76958e0473 | -11.42492 | -54.29737 | 2025-05-17 04:38:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eeb046bd-ded8-359b-b156-9c184f9197ae | -6.70331 | -42.12531 | 2025-05-17 04:38:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| ed7c5eb6-1303-3b64-991b-e665dea58271 | -6.84429 | -42.79684 | 2025-05-17 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 137cbdc4-1eda-32bf-949b-db26c49d128e | -10.53277 | -56.39054 | 2025-05-17 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a9e5131-d867-3ab0-bb0e-c1ed02f41b71 | -10.17078 | -56.80751 | 2025-05-17 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6af0cb63-05fd-34d5-8ffe-303fc6c137c1 | -12.35517 | -49.97319 | 2025-05-17 04:38:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f8b071a-e7e0-3a42-926a-87fa377608a1 | -6.75274 | -44.53533 | 2025-05-17 04:38:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b440f0dd-3602-33f5-af65-49992d4e27d7 | -11.27423 | -52.46571 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9096d729-a211-3ab0-841a-2dc61925debb | -7.23269 | -44.78147 | 2025-05-17 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9e944c8-be9c-3df6-9523-67b8df884540 | -13.31594 | -45.38396 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636c4ba3-c04f-3328-a18b-11e4d569fba0 | -11.6038 | -46.45786 | 2025-05-17 04:38:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61cb91d7-b9de-34f7-89a7-863e199b2dfb | -13.31438 | -45.39558 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df5fc8f0-880b-30c4-9401-911d6fc2ff30 | -11.91496 | -54.41071 | 2025-05-17 04:38:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a436f69c-3a11-3c56-a575-702a727eda72 | -10.31162 | -48.64276 | 2025-05-17 04:38:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb79584e-3ab5-3247-b49f-342a9caa04d1 | -13.31843 | -47.45878 | 2025-05-17 04:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8655392e-8c89-3ad3-8516-9b050d44953e | -13.32271 | -45.39674 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0212b13a-8160-3a04-bbd0-d8c386f3954e | -10.52943 | -48.59247 | 2025-05-17 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02161f70-2d92-33fa-ad2a-c9340fabf498 | -8.75047 | -49.75357 | 2025-05-17 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9461b68e-37da-333c-b1c8-6633beca867a | -7.95111 | -49.76186 | 2025-05-17 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5624fd8-f413-3eac-b05d-8ca7d34fe409 | -13.31906 | -45.39229 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e879707-bafa-384c-9cc2-a8777444cbc1 | -11.33889 | -46.50008 | 2025-05-17 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baca9cfe-3a92-3ed9-b7b2-0c0645b5e5b1 | -7.90245 | -44.4831 | 2025-05-17 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0abbfb6c-89e5-37d2-abdf-4ea4ff7ff9ac | -13.06098 | -47.82623 | 2025-05-17 04:38:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e123d9bf-d794-3820-8dd5-23467655e25e | -13.32739 | -45.39344 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e09a24e2-6595-39b9-b3b5-0194d8bb408b | -13.30083 | -45.36995 | 2025-05-17 04:38:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README10.md)
