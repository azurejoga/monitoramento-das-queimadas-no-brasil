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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 662b3502-37c7-3681-a7cb-be1ded728779 | -6.8802 | -43.06835 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60e4f74e-c8cf-3aa8-9eb3-5c24fbefca49 | -10.55665 | -46.75563 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df5696df-80db-3356-8169-c0472e4a50e8 | -7.55362 | -45.44519 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ac0ac9bb-def4-396d-9627-808dc41f2e69 | -8.35975 | -47.25297 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 384bd3f6-a9a9-3b3d-a7c3-8c5d2936f5bf | -5.40933 | -44.28202 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe0f0f52-d3b0-3a0c-850a-ed5bad60e9c9 | -11.42556 | -45.40466 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7021bec2-2804-3535-80f4-938c512442d8 | -8.76764 | -44.25782 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc414b31-76d3-3f72-99de-1210eb92773d | -9.62527 | -45.37967 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e07478a3-2ed7-306f-b6c1-a7edce2d9fb1 | -9.26379 | -45.94715 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fcb5ab2-a695-30cd-8a92-a79464538408 | -7.12587 | -43.10696 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1789e2d9-209f-357c-a34c-9f89c9ac2655 | -7.58429 | -46.73595 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fecbeecc-72cb-3a73-b4a7-89607663f24f | -8.79 | -48.71329 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ddf15cd-78dc-39b4-83a9-bfb4c8af1382 | -6.46387 | -48.43398 | 2026-09-20 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d9839e3-1d6c-3e26-87ac-768867975301 | -6.98817 | -42.20078 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 804766d2-783f-3e2f-98dc-c3fb8bb36af6 | -11.34493 | -44.18885 | 2026-09-20 04:19:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 332e0d83-26cc-38d1-9e92-3a0e29831573 | -6.97208 | -42.17309 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0160e63-5824-3475-9e0d-02ce9b09fab3 | -9.26568 | -48.21052 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b0971d6-012e-3b91-9535-86b567f548ff | -7.35399 | -44.4649 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c533f39-9b04-3ba8-9052-33d694bfd6f6 | -7.74527 | -46.71586 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36cff3a6-893c-3d4d-970c-63e6f744de4b | -10.45607 | -45.0926 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f230d76-df09-319b-bc33-c3d391b193f2 | -8.16649 | -54.74747 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f720b3ce-4d62-30f2-9900-0031c9fcb418 | -10.83991 | -50.94133 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8942cac9-8bf7-3069-bf3b-4fa0a2056998 | -6.00077 | -51.78622 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010de1b0-3a87-3a9c-bb4e-95bb5dd6d2a9 | -5.57807 | -45.5463 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0393e28a-e885-3d48-95f0-badf39761ce1 | -11.45928 | -47.64878 | 2026-09-20 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbd9c033-707d-31d0-b894-7f38b7b91457 | -10.27661 | -50.26794 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 426dc966-7613-3ce3-91a8-475cfe25595f | -9.8103 | -48.32152 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1953e008-2f43-3b4e-a3e4-c2627e5f5ca0 | -7.42838 | -44.73507 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc0f9781-62a6-3cb2-9488-56861781b8e2 | -9.7858 | -45.06376 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 744b82ff-6615-30e9-9266-e2f897e43ccf | -8.62782 | -47.62041 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 319f1606-c546-382f-a76f-e3f19c6e9006 | -9.81864 | -46.38863 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c6f44209-b92f-32ca-a791-525d4821e3ac | -7.3491 | -44.4724 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8b5a362-79a9-3e9a-9c9c-62992dc68786 | -11.01824 | -48.30054 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f826a558-0b03-35e8-b728-0c67d4f2cb1a | -11.66566 | -43.4179 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bba7e3e8-cd27-3f0e-8acb-83c8e6310ce1 | -7.18275 | -47.89614 | 2026-09-20 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 51c3c46b-45d6-3e47-acd5-04ee179e807c | -8.66699 | -45.4347 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4479d82b-9605-3f41-a1cc-adc5094365bc | -8.93262 | -44.39216 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 337890f1-6b92-37f5-bad3-3e5c0df85502 | -6.19334 | -45.33133 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08e744bd-b652-34ff-a9fb-96b208a59287 | -6.30634 | -47.62639 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67be7688-8110-3095-9236-2a2de9bc75ad | -8.75789 | -48.6603 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b080f9a-b441-3d4f-8088-1e77be2f54b4 | -11.45592 | -45.39752 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fec0f6bf-aa5e-3b2a-b77b-4ba867f20187 | -7.43936 | -44.75799 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 661dff99-7903-30eb-acae-dabedcbff074 | -10.4596 | -45.09324 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab0e99d0-19bd-362d-8316-a9367de27743 | -5.85118 | -53.50209 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f45dd6e4-c10d-36b3-833d-2cb1f2ae58d4 | -11.49714 | -47.78764 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 831c0e5d-d011-39f8-aa30-7286a1ba8374 | -10.20788 | -53.92225 | 2026-09-20 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a77c7ef-f4e8-3bb9-bc88-c04b2bc4350e | -9.66788 | -54.3221 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c6d1386-196d-3e44-89a0-3dddaa44278e | -5.84644 | -53.52854 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6fe708f7-7b3b-3594-8db3-90292ef74eb1 | -7.95638 | -45.24146 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41dcdbf2-0e01-33f5-acd4-402ba9c84cee | -7.62525 | -45.45989 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44d263fa-1828-3869-b141-2dc7095a708c | -7.02822 | -42.07824 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad8a6f79-c766-33a3-9ff4-4a33b50a0998 | -5.85547 | -53.54949 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56401d2c-deef-356c-9def-fbe45a752c9c | -8.05161 | -46.27995 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 63615794-1e6c-34cf-8ee0-84300eb3351a | -10.7865 | -50.87415 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6430ff97-c88c-3589-9998-0d11097f9b05 | -5.23864 | -47.58571 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1049d4-e3cd-3f16-b501-1b4624066dbb | -5.84549 | -53.53386 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6890f29-e3ce-3991-ab3c-66915f8ba8d9 | -9.26415 | -46.19639 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 78178310-cc34-3041-838f-38b100fd3013 | -5.78796 | -42.56607 | 2026-09-20 04:19:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 76561357-1aea-3105-90a3-0085c3d85b31 | -3.97681 | -48.93112 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8bda3fde-7d8a-3b3f-ab17-3acb510e4d83 | -7.4963 | -46.71344 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c2a4659-d6c1-379c-b912-9000713103c8 | -3.40005 | -54.07146 | 2026-09-20 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fd0edb9-804b-360c-a942-f2c7da9be8ae | -7.53426 | -44.93056 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fc98a00-00a5-306e-b926-337e2b1b257e | -11.44546 | -45.32962 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e6517ff-d702-3c08-a2db-504232452081 | -10.58302 | -46.53398 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 602f95d8-655c-3e79-8b14-25fbeb690bae | -9.37583 | -45.37476 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22490663-df7b-31c0-b09e-49e6b5b782a7 | -9.72746 | -47.26541 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d7c2541-6946-394d-8dac-20812088377c | -9.22007 | -43.17902 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0bd42ccd-a04b-3491-8d77-1a23bc3f2c54 | -8.17317 | -54.74875 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89f3df59-07eb-3029-87b8-05fecfb403fd | -9.02421 | -48.74269 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e4fb247-0eb5-35d1-8997-459d20060bde | -10.2088 | -53.91755 | 2026-09-20 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afde94b3-2d62-30d7-b6bb-9990ef30b01d | -11.00581 | -48.3213 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32bb52ba-0da9-3a74-bbd8-ee34499c4e37 | -9.45973 | -45.43041 | 2026-09-20 04:19:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b689ee4-e93a-3fa0-9ae8-bf279a3946f7 | -9.26563 | -46.21074 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b47e04b6-f748-3714-ba33-852f61eeff66 | -10.48721 | -46.28241 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40753223-e09d-3cd6-8cbd-53503d3d9f9a | -7.58264 | -43.43448 | 2026-09-20 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e1cefc-7afa-37b6-b23c-c5480bffacd0 | -6.45768 | -48.44245 | 2026-09-20 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 050d08ab-2c3d-3a72-a844-84832c88c721 | -3.4065 | -50.40156 | 2026-09-20 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37361d83-3703-3e0c-bb77-1df8d1680a49 | -9.16985 | -51.51255 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca40ce2f-1060-31b8-b2f8-d33ea3d848d2 | -9.9019 | -46.53138 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a0719f5-578b-3e5b-a7d3-8b460da52c0c | -8.76431 | -48.67593 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 844eadab-1462-3b16-9e85-e8a724ae8898 | -8.18098 | -54.76837 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d40797bb-6de7-3667-9148-2b5326a357de | -5.84058 | -53.55768 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8cb9ad0a-089c-36f8-9c5a-bb83cae839a9 | -9.83972 | -46.4256 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fe4f1d9-5dab-3e73-b81a-54a5369c5de9 | -6.25363 | -41.6905 | 2026-09-20 04:19:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a8df1481-6c3d-3e39-8a2d-239bfbc17909 | -7.96106 | -44.06749 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55e75f42-a597-3845-b671-234c61cf9982 | -10.4121 | -48.93972 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 978c9af8-ef37-3f87-b6b7-8cf8dec2d652 | -9.90082 | -46.52938 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 402bfd87-67a6-3abe-8d63-ca873b8b6845 | -3.90285 | -49.06847 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 231b7f2d-1b83-3ce5-9a2f-dd25e57711de | -11.06336 | -49.73973 | 2026-09-20 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af448138-3790-3c2a-9bdb-5081e1816923 | -4.07377 | -52.12271 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae927a34-9502-3b81-9983-3bab7bd15df0 | -8.60657 | -54.61132 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce028621-5fe7-3d3a-9732-ff03b43651ee | -8.26202 | -50.85635 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bed2af2-e16d-318f-bd1f-ecc1999eef4f | -9.56347 | -46.55739 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 339cab14-7194-3445-836c-42019104a4ed | -3.97757 | -48.9325 | 2026-09-20 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 905f3649-43e5-3669-8116-21125dff0477 | -9.26083 | -45.942 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03ad1c0d-ba2c-3cdd-8e06-508ac7be0ee8 | -10.46445 | -45.08583 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b64dde8a-39ff-3b97-ad4b-6d01dcc80139 | -11.45422 | -45.36419 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84d2d570-ca27-386d-9bb7-742a75365e13 | -6.16856 | -47.51568 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 37c63f89-b6d2-3597-ab36-4527b5f63576 | -5.79657 | -43.77113 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1da6230-904c-3bcd-adc4-730269b162e1 | -9.224 | -43.17599 | 2026-09-20 04:19:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README37.md)
