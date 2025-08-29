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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cdcf22f-5603-34a8-8198-9cffe4d6a2d6 | -12.43528 | -63.91723 | 2025-08-29 05:08:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 296d2588-25b9-3da4-8d1d-a3bc9d5bf28c | -11.5762 | -46.2662 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be4380a-1155-38b2-af82-2ad12c2710e3 | -9.16526 | -59.555 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| daa045b9-d149-3fab-9215-10bb9e8ae01e | -10.84698 | -60.8232 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b231aca-a63b-3232-b91e-8678b724acb7 | -9.10816 | -65.77853 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 45d0d2da-e3a7-38c0-ab3b-d46317da96e4 | -8.28123 | -61.40267 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98c80eb8-effb-37f0-a32c-36ee5c5f96ed | -15.16991 | -52.32719 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37343ea7-bb1a-31fd-84a5-466cbd47dde5 | -9.46737 | -60.31112 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 112debae-6d0d-376f-a585-ddde59e4f2dd | -12.08605 | -44.72294 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf3217ba-f5e0-30ad-a067-722bca852fa4 | -9.22019 | -60.86821 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 25228dbf-8d78-32cf-bb8f-cedf64243053 | -9.91689 | -54.7255 | 2025-08-29 05:08:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bf610ae-cb97-3803-9f5a-bb5565b3b35f | -9.16153 | -59.53266 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8d779ee-57c7-3a35-80f1-22e93c3c24e4 | -13.55401 | -46.86629 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1468c62-842e-381e-94a6-3a22d4a51739 | -13.5951 | -46.86678 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| deb95b32-f758-3768-8be3-f21df0a26bdf | -13.50907 | -46.85201 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2df68a8-bc60-3fa7-8b8c-42b9e012b146 | -9.15719 | -59.53627 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cadd5ea6-f5c1-3c36-977e-3c5348628c9d | -9.32106 | -56.90721 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ece2b341-2366-3d71-8865-54a2c70b628d | -8.17506 | -61.36572 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3034819f-a47e-34fa-a0e7-5b30d457cdad | -10.45803 | -57.94428 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28edb581-f250-3173-ae24-bbdf20443a26 | -9.79465 | -56.60943 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1744a9d1-0c30-3ba1-9779-444e27033613 | -12.68719 | -48.19511 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 68ddd692-48b2-3342-8d54-bf8991b51892 | -11.6122 | -46.20436 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1d73822-9680-39ad-a8d9-22da4ed26eda | -11.35001 | -43.54541 | 2025-08-29 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08cc55ba-4a87-3a37-9e0d-dd3c8251aa5d | -13.48655 | -46.84349 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a42ea174-9b7e-3696-9600-d23d6af5feec | -11.16246 | -47.15432 | 2025-08-29 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c27d53d-d62f-3fa0-afe8-543b6870a315 | -9.31189 | -57.70593 | 2025-08-29 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c437d903-a72a-31c1-b615-e21eb2b62d66 | -8.2875 | -61.41529 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3f8d202-8da2-3768-a37c-57dcda25bab2 | -13.67158 | -46.92066 | 2025-08-29 05:08:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab88f3ee-8c82-3b7c-bf8f-838dd5152828 | -10.03528 | -59.35921 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b6a7517-1c90-338d-892a-440d7030b819 | -12.0854 | -44.72847 | 2025-08-29 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26690d8f-4f8c-33cd-ae9c-793c9051d0b3 | -10.48512 | -57.95187 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0148a99c-a37b-3978-86b2-31b1f587ab5d | -13.54233 | -46.86563 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c4b7460-7459-3dab-8964-8c52708390d1 | -11.60803 | -46.20276 | 2025-08-29 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ceca00f3-5e6d-37c3-b447-6ad82e99fcb7 | -9.9394 | -46.70738 | 2025-08-29 05:08:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcec9086-f149-3b6f-940a-7f23657a2ce1 | -11.88067 | -46.41021 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 299312d9-288c-32c7-bcbe-1002a992590f | -9.78285 | -64.24812 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 32ad5dec-08fd-3f96-bb6f-d016a074be5a | -12.88586 | -48.13293 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b182e35e-0e3b-3f55-8eb1-77dbd752d4af | -10.34866 | -59.19387 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ab62995-16e8-3345-a328-0e8feb33b1a3 | -8.94939 | -65.96274 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e54c67d-e02c-33fd-9c78-7d331c7a519d | -8.89875 | -60.56479 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98c68844-87c4-30e9-8f5a-f3941a0383e2 | -12.83817 | -48.17281 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| af3f9252-4dfb-3ac9-be2b-44d4782de0d8 | -10.49402 | -51.61491 | 2025-08-29 05:08:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ffcad3f-0fa6-3309-b929-f5395dfba5fe | -13.58878 | -46.87059 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6f0a00-579c-389c-8cb3-ec71437ace97 | -9.77898 | -64.24187 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff006709-49b3-3e6f-9ad3-09c8c0aa6d4e | -9.45891 | -60.5693 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1dd2a4e-af91-38e6-bcaa-6deedc83b48e | -9.80229 | -67.84846 | 2025-08-29 05:08:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bff2f201-68f4-3ea7-8647-9b5d667cf7f4 | -10.38334 | -57.82802 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e10036-d2f9-39f0-95ed-02c0c60c4676 | -9.29894 | -56.80997 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e7c8a09-66a4-30f4-919e-19431bf745ca | -13.55263 | -46.87839 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab6b1675-1a9e-32eb-a7af-8a5ac2cf2960 | -9.12005 | -65.77126 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 47494661-5576-3915-a0c7-60463da7797e | -9.15221 | -59.5659 | 2025-08-29 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fdb95014-b3ae-3a17-8ede-46065229ed15 | -12.70294 | -48.19715 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fc4c0e9-0e56-382b-b7c5-59d098040b63 | -15.16846 | -52.33785 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b221ed0-671e-30fe-ad86-bd8f88f5b3e4 | -10.8451 | -47.50188 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3297c25-3cd1-37fa-afd4-6ab8b4a78776 | -13.02589 | -56.91719 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4525722-86bf-3e31-a81b-6187052517f5 | -16.28205 | -53.61512 | 2025-08-29 05:08:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a701407-2fed-336b-9514-b8f9e1b33847 | -9.41054 | -60.57551 | 2025-08-29 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40126604-0a46-338c-9a21-fb7f455a0583 | -10.67989 | -47.08565 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a49e44e-d3ca-3369-860d-65b6e454a83c | -10.29304 | -64.49206 | 2025-08-29 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59e83389-b765-37b8-af8e-55577c4f978a | -11.31281 | -55.22127 | 2025-08-29 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4a88faf-3b35-375f-9286-7b914afc9730 | -15.81667 | -48.16683 | 2025-08-29 05:08:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b5976e5-ec5e-352b-984f-22c05216ad7a | -14.58658 | -54.5241 | 2025-08-29 05:08:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6821e6d4-6ca9-3fd4-bc72-7477d8e06b06 | -12.98938 | -56.91889 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ab86869-3d8d-36dc-880c-4e8e99dff719 | -14.30677 | -53.29472 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ae1b0e6-7d67-32ca-9763-4dfd1cfb871f | -15.21161 | -53.79486 | 2025-08-29 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb043adc-12ba-3d88-a8f9-62e6fda0e821 | -10.979 | -46.91996 | 2025-08-29 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 353ff2a6-e602-30c9-a8d5-2d2698169283 | -8.18546 | -61.37885 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 065b0caf-5b05-3345-921b-7469d80d0a6c | -9.29838 | -56.81348 | 2025-08-29 05:08:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd07eb1-1b23-338f-a0b1-3839fc323163 | -9.12158 | -65.76686 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d451d83-00be-3422-bda0-b95260f812b4 | -9.76542 | -64.26154 | 2025-08-29 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d609f857-fc8e-36d8-8410-670d661bd50c | -10.85876 | -60.81283 | 2025-08-29 05:08:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 300c1af1-341d-3325-a076-2746bfea17f6 | -8.95489 | -65.96378 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24f2e397-953a-37fa-88ef-e5dfeb298834 | -13.19627 | -45.282 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29046793-ba7d-39c0-9f90-c71fcc2fca21 | -8.1099 | -61.21575 | 2025-08-29 05:08:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 547d5a33-f51d-3309-88e9-4381cfbe1d03 | -8.9514 | -65.95172 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0823e0-2541-3376-88df-237f28b8427c | -9.11278 | -65.78046 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c6d5940-dca8-35f3-b187-32b70aef7cbd | -13.01047 | -56.91505 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a871f572-89a2-32d9-a086-047b1a1f07c9 | -9.15216 | -65.78328 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 420deac7-94cc-38c9-9266-31f3750e3b77 | -13.00714 | -56.91451 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6e4733a-e2c3-319f-9e2e-53fde1a5c365 | -15.18951 | -52.33713 | 2025-08-29 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ead3620f-6fac-3708-9b37-467b92945ea5 | -12.08826 | -44.98568 | 2025-08-29 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3293a5f1-8ee2-3194-9c2d-51a5cb3c3c2c | -14.30101 | -53.29654 | 2025-08-29 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 620bc211-0a0a-3e6a-9b5e-93f4a08321b3 | -13.18353 | -45.28049 | 2025-08-29 05:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ec013765-14b8-3c0a-883c-85dc3bfb7eda | -9.11943 | -65.77467 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6368a1f5-4af7-3391-91e1-89b794206cc3 | -10.8119 | -46.35891 | 2025-08-29 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb35e1ae-81d1-3609-937d-e286b9e9f54d | -12.83465 | -48.16171 | 2025-08-29 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f46c7714-6b8d-399c-b3dd-fba5f44ef21d | -9.9354 | -46.35662 | 2025-08-29 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f418b099-4ad5-3513-90fd-28cc1c1ac850 | -9.1307 | -65.80804 | 2025-08-29 05:08:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfa1e2b1-508d-3ffa-b2df-a2d5bc01d52a | -10.46932 | -57.93874 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7230173f-01fd-3dc4-8c52-eed2c41c1b25 | -13.01646 | -56.91201 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6eadaada-4e64-3c8d-8daa-43e3c45bcff1 | -11.56787 | -47.62289 | 2025-08-29 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc4c46e1-5ce9-3a9d-b733-1c0616e13933 | -12.99327 | -56.91588 | 2025-08-29 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 575f031d-2363-362c-b682-422290d4ddc9 | -8.29289 | -61.40854 | 2025-08-29 05:08:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcd2e524-897a-311d-b41e-db42862d4bc1 | -10.36806 | -57.82928 | 2025-08-29 05:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 189d03b4-1a1d-3b1f-acfc-7db2e82eead6 | -9.54297 | -62.4016 | 2025-08-29 05:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 599efc4f-4623-3e1e-b637-095fab127595 | -10.46991 | -57.93512 | 2025-08-29 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22d704d7-b9e6-328f-a72e-10a58fa90918 | -13.4099 | -46.84245 | 2025-08-29 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cdf4f2a-2a20-3e29-9ab6-196768ecc3d3 | -10.61421 | -54.91042 | 2025-08-29 05:08:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4f0833-d8d3-37d4-8d8a-74492f785423 | -13.35682 | -54.38771 | 2025-08-29 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8253840-3ca3-378a-bf59-35e18e16bb7f | -15.53984 | -54.27388 | 2025-08-29 05:08:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README64.md)
