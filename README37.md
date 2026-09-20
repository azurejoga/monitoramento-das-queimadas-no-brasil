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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 719fdd6b-327f-3c30-831b-abe35a95c287 | -6.19793 | -45.32489 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d3e41fa-3391-3e86-a722-b39bd178c7c8 | -10.83726 | -50.93709 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1bff9cfa-c74a-32ce-add6-33373bb694a6 | -6.53508 | -44.94653 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7ca26a0-9674-3319-9697-2ab5c75bf78a | -11.08909 | -48.29239 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f98c63e-b799-3344-b4f0-dc993b39bed6 | -11.10411 | -49.51081 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d190faa-221d-3ab1-bfb0-b5f8c4ef52f5 | -9.0218 | -48.75629 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86a0edde-43e2-3d2b-ae8a-d27c069ebcf0 | -6.31938 | -47.62866 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d0d364d0-d390-3931-ac0a-f22570ac1984 | -8.84621 | -44.9194 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2be26da6-dfc1-3adf-9472-81b01a69168b | -7.62951 | -46.7617 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83a500f1-cbf5-392b-9a53-3236bcb33abf | -5.8438 | -53.50611 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e8357a3-f433-37b5-9428-345aab589e7c | -9.27901 | -48.24524 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6834a51a-39ba-3a25-b0cc-ebacedd81700 | -7.53202 | -45.43711 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| dc662da8-d4f8-344c-b37b-bf22c4e87170 | -5.85562 | -53.55185 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d14140c3-8fbd-370c-802a-38bcf30bd2b7 | -7.97148 | -44.06916 | 2026-09-20 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9a91799-1445-3399-8aca-eb474edb88ed | -9.77446 | -45.06599 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0882c19a-4995-39a7-8798-1a60a0d4c5f6 | -7.58892 | -46.73311 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a2f930e-19ad-3b29-84bf-e01040aaee74 | -7.62995 | -46.12027 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ce7c7f-20d4-37cd-9293-c5af411603e3 | -8.7689 | -44.25025 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70639b8c-7f82-3714-bb77-c7cb437c26cf | -5.66787 | -45.30504 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d6252dc-9523-31fb-b52d-ac21469f793a | -10.46158 | -45.0812 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd73d528-8d81-3b1c-9d8a-374f2832ba9e | -9.21681 | -46.22194 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ece0234-7dc1-3118-80b3-8b7f8c502c44 | -9.55247 | -46.57562 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0662acf-4fa5-39c3-bc07-da4272d2e86c | -11.48602 | -47.75593 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ea6f8b1-4f51-31df-aa1b-d3d978ec9f5d | -7.77463 | -44.83092 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d16f099e-98b8-3ea6-a181-4ea00096f38c | -7.43216 | -44.75686 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 92c58aa3-55e2-3a90-94e4-2ee113822835 | -10.77697 | -46.32891 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0db2ad79-5005-390c-a8d3-5a230e04f34c | -9.85516 | -48.34367 | 2026-09-20 04:19:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32e3607d-41ae-37d0-a20c-9c3d175d8c8b | -5.66817 | -43.40983 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5b03477-23ab-3a99-ba44-ee1ad5c68c2f | -8.76068 | -48.6704 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5b1759c-392b-38c4-8d86-94ad03cd11ef | -8.45004 | -45.86581 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03a6adcf-ed39-3a03-bf2f-6ff226735027 | -6.77657 | -48.65945 | 2026-09-20 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8199facd-eb5a-371c-96a6-bdc888838b21 | -7.5766 | -44.90127 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69c49937-f36d-3687-a30b-4259ccbfc36b | -6.28081 | -41.77674 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3bd8781d-5519-3f54-8ef7-2e20d53cce14 | -6.30491 | -47.63481 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b8a26142-a099-3e04-b019-8e4f98409e53 | -7.41946 | -44.69991 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5498e092-5a69-3c30-b34a-e40a64952b79 | -8.17541 | -54.76117 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e2d5bce-4e96-3828-a290-99ce254004d7 | -8.7681 | -48.66894 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dbd8eecc-666c-3e04-820f-532656d14dd3 | -7.16391 | -47.43325 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a20f67c-4d84-300f-aaf1-087e54fe9427 | -10.38942 | -48.98977 | 2026-09-20 04:19:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91a060fe-1c00-3b00-9b27-193ee8b8fe3c | -8.1835 | -40.8221 | 2026-09-20 04:19:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5561b833-51ea-317d-85ef-ee19fdfc3521 | -7.74481 | -46.76702 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a52f7d84-2462-36cd-9d3b-5fcf069ef2d7 | -4.68529 | -46.39897 | 2026-09-20 04:19:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 69203c43-8854-399e-8e5f-95635aab02e9 | -9.22298 | -46.20879 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6224cde2-8b85-376f-b234-cf6b97ef3dfe | -5.85669 | -53.5085 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51c37d13-bab3-3bd9-b8c4-8a30092d540a | -8.05795 | -46.266 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2da6b8f8-2fc1-3bbc-9af6-c8912b815568 | -11.03581 | -48.29937 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb568e2e-8804-3d88-93df-184a8c8bf8c7 | -11.47976 | -47.79171 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e71349b-855a-3ca1-af09-c48ff549302d | -9.66667 | -54.32019 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4848202d-e0fe-3460-89a3-a6421100570c | -9.69487 | -48.3141 | 2026-09-20 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a9b462e-7ddb-3b6c-96a0-e8b195abb0e1 | -6.97878 | -39.88725 | 2026-09-20 04:19:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4452fa62-236a-374d-ad77-63ff17e2bb97 | -10.45131 | -51.24963 | 2026-09-20 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c268f434-e827-3df1-9ecc-3b9ee6c176b3 | -8.01785 | -43.33553 | 2026-09-20 04:19:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8d044328-e34c-322b-8fdc-56cba79aebef | -9.79135 | -45.05228 | 2026-09-20 04:19:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b73ae54-9b17-3dc6-9e51-04169960853c | -9.89237 | -46.53266 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 673817e8-12dc-332d-884d-f4419c37e935 | -8.2984 | -46.86213 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 850ae5e2-c274-310a-b205-a29bb010f53e | -10.77621 | -46.33342 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e12cf91-eac6-369e-9bfc-af25cc73310b | -6.98561 | -39.88838 | 2026-09-20 04:19:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 504c5280-883f-30a4-a70a-fe6e713e4dca | -10.13007 | -45.55293 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ff181a0-db33-396b-9543-f3c2f50a2792 | 1.01899 | -51.1892 | 2026-09-20 04:19:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdea716d-28e9-36f9-9c82-7a144432431f | -7.68805 | -46.10531 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a56b97a-35ca-3645-9cb7-b3ed8ebdcd14 | -10.47345 | -45.09451 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62fc412a-fc63-3d51-9540-22b131fc35cc | -8.24738 | -45.60028 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8254a819-c169-3f39-a52f-9ca71d3e53ec | -9.25493 | -45.93148 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2839901-cc72-3824-8860-29c6f1789abf | -6.47621 | -43.9197 | 2026-09-20 04:19:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be189ace-07be-3e7e-acc4-2e96dd005c0b | -5.85095 | -53.53785 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c11e01e-821b-381c-952a-cb30504e6b98 | -8.76361 | -48.66822 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c3e7fe6-d022-3149-928e-eb91f7d9157f | -7.15637 | -47.47675 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b50e135b-f839-3a10-81ba-18e885bbabf5 | -9.05137 | -48.71944 | 2026-09-20 04:19:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5ba4b973-3fa7-3311-80f6-81f8ad31de43 | -11.49777 | -47.78405 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad009533-995c-3be5-9201-f52ba790e70d | -9.80525 | -48.31699 | 2026-09-20 04:19:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96328f19-dc8f-39f3-a1a4-f0f2e49b0652 | -5.89145 | -46.58707 | 2026-09-20 04:19:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2644f8f-78b9-316e-bc89-a55a88f18ec3 | -10.27759 | -50.26254 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e0479a1c-bcb4-3ca0-8bad-3263501a1084 | -11.43129 | -45.41397 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1efa73db-e506-3816-aa4d-a4c3d9658c77 | -6.38893 | -51.67857 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf7c13c6-889f-36fb-a3ce-cc69223b02ab | -6.71961 | -46.07894 | 2026-09-20 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe1250fa-17d3-3dac-a545-4bb5d8fc485a | -11.08845 | -48.296 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e9395d6-2712-30f6-94fc-640698d20e67 | -10.92915 | -48.31387 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2e2c184-fe25-3bbb-bf4b-2ba7c0b4db23 | -9.0491 | -40.30115 | 2026-09-20 04:19:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a7e14a8b-ae02-3f4e-88a2-0db5b9682415 | -6.71965 | -44.04249 | 2026-09-20 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 685fd559-f3b5-3e5b-ab71-fdefb0de77f0 | -5.23928 | -47.5549 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f25c234-7bb6-350f-b4f8-1046ec2f49f8 | -6.94972 | -43.09401 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fad39ca-8796-3a0f-9360-cafc08996e38 | -7.52693 | -47.33617 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58138745-6da8-3b63-9442-f299669fe775 | -8.45323 | -47.65424 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af02c7fc-f42f-37bf-94d1-1a23f259b3ce | -7.7504 | -49.20349 | 2026-09-20 04:19:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76616171-56b2-3c5d-be86-b0c9c16b990e | -10.30963 | -50.2519 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49f5a63b-54b7-32a6-951b-261b8c3c34dd | -6.9489 | -45.61942 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1440f5c8-23b3-3fd1-876a-849b25239d0f | -4.77592 | -48.05519 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07c325fc-6bc6-3291-b5de-b3a9e4f1a396 | -6.54585 | -44.13512 | 2026-09-20 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 438c0952-92f5-366c-9457-faf4e024a678 | -8.16872 | -54.75989 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 630e9876-0d61-3bad-912e-b3f8934d20bf | -5.46217 | -44.32021 | 2026-09-20 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a1c519d-489c-367b-a3ea-a61511738e78 | -8.14261 | -46.80177 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa7c58d0-c2ca-3dae-bf4f-55a4fd5ede83 | -8.75705 | -48.65276 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9937fddd-789f-3800-bf63-1985a84c025e | 1.21943 | -50.98925 | 2026-09-20 04:19:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d581df6e-b639-3bc4-b712-380d4b843b6c | -7.62669 | -46.75399 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1a4cff6-e361-35ae-8195-d62daa0c8467 | -10.29798 | -50.26084 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 4dee62f4-8a46-3b95-9471-768494df6a63 | -7.54911 | -45.4263 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 57a6b2ab-f7b5-3f69-bfb3-40fc7fbf225c | -10.23951 | -45.34879 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 454b0206-7d72-32e7-be19-d39a404d42ab | -10.2874 | -50.20867 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7403aea-7106-32ad-9e61-0fc15ac0e7c4 | -7.37023 | -44.86173 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ebd79f5-3e4f-3e27-9b30-29fcd9d56c99 | -3.49947 | -53.43911 | 2026-09-20 04:19:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README38.md)
