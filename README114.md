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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9df9123f-edcd-395b-b08c-fbdb5a42884d | -9.63435 | -61.82436 | 2026-09-23 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1b24256-fd14-3f01-be0c-9531ea07d429 | -3.59583 | -59.11036 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fefa520-a73a-32d6-ab63-860ae6c873b4 | -9.15807 | -61.19196 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1f02679-6f67-3159-bffb-ac666d6f470c | -11.66407 | -50.88725 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c2e984a-99b7-31a3-94e2-9a384898a3f0 | -12.36179 | -50.15259 | 2026-09-23 05:23:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 675e4a94-bd3f-324f-a946-95d1ec517393 | -3.1514 | -57.6897 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d98d1491-6b8c-3a5a-8415-dd65ee63fe0f | -3.12866 | -61.06253 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cfd0c4b-7268-3aca-b375-f54b3fa261ad | -8.92065 | -61.49069 | 2026-09-23 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efe39814-39bf-35f0-974d-6f878ca852d8 | -3.29137 | -57.85728 | 2026-09-23 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eecf3543-07cd-3bba-b883-cedd242f4288 | -5.1822 | -56.17964 | 2026-09-23 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46ae6414-d66d-3017-91fb-3d8857d74e56 | -3.77642 | -59.60063 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e02ae7-23d1-35ec-a6b9-5bfc9dcf281e | -2.73225 | -58.02083 | 2026-09-23 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea4cdab5-6a66-31fe-a78a-0cc971c14b21 | -5.61421 | -45.25431 | 2026-09-23 05:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b7d1fe4f-feda-331f-bccb-66ccca516e6d | 1.91055 | -60.57786 | 2026-09-23 05:23:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cdf3175-8360-34f0-bed8-0243315ec330 | -10.32561 | -50.51068 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412aa421-e6ec-33ba-bf27-a2f5f773060d | -11.1316 | -51.05511 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f759f229-9989-373d-95c0-0970bd13c9bc | -3.40304 | -61.2916 | 2026-09-23 05:23:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83420685-8f82-3e56-ac3b-01070ab61aa7 | -10.28813 | -50.53502 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 832b3e1d-d5d5-3e77-810f-3e2e66f809cf | -3.78919 | -59.70737 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53142509-33f5-3cfb-97d7-1b3d14e82b42 | -3.58986 | -54.52139 | 2026-09-23 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76df4daf-78bc-35a0-8a2c-78de204fb46e | -4.26876 | -55.44319 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95828d42-6b85-3046-8e13-9fc6aaed34b1 | -3.5864 | -59.06274 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85eb6f84-1baf-392e-93c8-e7e1b2919c4e | -3.86173 | -58.89064 | 2026-09-23 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f68ef81-a61d-3ae5-923b-339fc19a17d3 | -10.25561 | -49.97004 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 014e004a-2731-3113-bacb-8146a20175fa | -11.64228 | -50.95473 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 777cf29e-4259-3cd5-a76e-7ba277aff841 | -5.57332 | -52.02396 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8360d119-9c70-326c-afb0-344e70ec9d0e | -3.89249 | -60.59182 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c782853-fb27-3064-94fc-916e7d9f1d7c | -10.84447 | -56.21643 | 2026-09-23 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ebeac5a-4509-3928-bc3c-0a47e36f778c | -9.10386 | -61.4414 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9880e146-6bdc-3962-b35a-25b33abdbcd7 | -9.15587 | -61.18416 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ab1dffe-12e5-3a6e-9d48-200aaab48422 | -4.25724 | -60.00717 | 2026-09-23 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6424c309-fcfa-3bf0-9774-2b9487ec7432 | -3.91903 | -60.5579 | 2026-09-23 05:23:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f1daac-3f59-3cfb-9612-a915de4a55d4 | -4.2786 | -55.4275 | 2026-09-23 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88743144-5f4b-3177-9a01-3b6f814b8be1 | -6.43554 | -48.45532 | 2026-09-23 05:23:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06a3cd79-eda8-347b-b293-7a14fce4198d | -10.27511 | -49.97658 | 2026-09-23 05:23:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1f852961-253b-37d1-a760-c2c7f1753b43 | -3.44985 | -58.18678 | 2026-09-23 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e98b5e-2cfd-3e7e-aa53-1c6c7fe81c31 | 2.31884 | -60.92036 | 2026-09-23 05:23:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92a1abba-8d9f-3439-b6f6-f65a45767c75 | -11.10454 | -51.05495 | 2026-09-23 05:23:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d8ffdad-93fe-3991-b4b4-698995b86c31 | -4.15833 | -60.79113 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb27b0c-1c49-3361-8451-a84883aa2844 | -12.41197 | -46.97838 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8448ca47-7f12-39d8-b66c-e94fc03ea3db | -9.87109 | -48.39549 | 2026-09-23 05:23:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b345c250-84cb-385d-b738-1b32923a6a92 | -11.69357 | -50.78297 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2afcc4e2-5e2d-3f90-9a9b-66f5fd265533 | -12.41132 | -46.9713 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b12e4a8-f43f-3c2d-b239-bbf0789f04ab | -5.8903 | -52.09652 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c524073-c97e-30ec-8312-af12e345aef1 | -10.29829 | -50.50703 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| be6af20b-f7bf-3fb1-8451-f22f8e057550 | -3.39348 | -61.05912 | 2026-09-23 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 477e82ed-5e99-36e5-b7fb-50264ed89bc6 | -11.77919 | -50.99435 | 2026-09-23 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed5690f0-2475-32da-b28f-77a1760c9ddb | -3.1062 | -60.7066 | 2026-09-23 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 271e1857-ed0c-376b-9291-431fa1183b83 | -3.25011 | -53.95301 | 2026-09-23 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4372148f-0e20-34be-bbbc-1c8cad7f3da8 | -2.564 | -57.51644 | 2026-09-23 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 076d1edb-36a8-3cfc-a4bc-6e17005bbbee | -9.10166 | -61.43349 | 2026-09-23 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c8333f1-3f09-3523-b526-c912ec0f7b96 | -12.41902 | -46.96547 | 2026-09-23 05:23:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1eb8b272-32a9-337b-984e-f2c22d194598 | -10.28795 | -50.54541 | 2026-09-23 05:23:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de4fd5e4-0ff0-3baf-8c4f-5b0a20e957de | -4.56259 | -54.94163 | 2026-09-23 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 816c95ee-2044-3642-a795-ab07c3976323 | -6.78913 | -48.68643 | 2026-09-23 05:23:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82a33e7d-31d5-3bf5-b621-d2331163d168 | -5.81021 | -47.76347 | 2026-09-23 05:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43d7df6e-fd91-307e-bce7-53e363f237a2 | -3.68613 | -60.63316 | 2026-09-23 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94ed1b44-7c2a-3351-8cbc-e6f99930a268 | -10.95803 | -50.6104 | 2026-09-23 05:23:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61ef0df6-4d34-39ef-aa38-fe276371caea | -6.67865 | -55.06481 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7b59655-1f2b-3f4b-96a2-0e8ea168f3d4 | -6.7111 | -59.00258 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20479f41-a4d6-3f99-a076-cb35a45536cc | -5.8219 | -57.74072 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b9f40d1-fd33-3273-9eec-b216b79f36d4 | -8.20362 | -54.71913 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd362739-9219-383b-9e58-7b8c21b98827 | -6.34288 | -57.86111 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8eacb18-2c00-3280-8d90-543625d13856 | -6.72648 | -59.44123 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6b5d76a2-4273-3520-b59d-f454df8975f3 | -6.687 | -55.06115 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43c492cd-f1d6-3847-afe7-88b6bf8d03f3 | -6.31391 | -57.74708 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4d94c01-1680-35e5-94cc-c2bac445c1ef | -7.54648 | -57.72701 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c20510c6-083c-328f-b923-0bf934a07e35 | -5.80316 | -59.22346 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f083189-d1ae-3dce-a2e0-007ad09c1468 | -8.30763 | -54.77329 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 902ac975-5976-39fd-8c24-c31cc017c6c8 | -5.27922 | -60.2089 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30c01a97-6c27-3b7b-ace5-450f03a3514d | -6.31643 | -60.05085 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a832ce2-03e3-3936-88ad-2aa984e92f64 | -6.12195 | -57.76163 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df665cb-1c56-3a46-9b8d-e6cffd71cc60 | -7.39463 | -55.21928 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 166b28c5-019e-30b9-acc8-5144e816e2ec | -8.23646 | -54.67524 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 008ede36-0b78-3f14-9e2d-da91de46de32 | -7.38824 | -55.22998 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b7d8645-7707-35db-ad7b-ad88667ef0c1 | -5.80707 | -57.73557 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db1a3524-11d0-300f-8020-56e9916246f5 | -7.29695 | -59.52894 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efd7e8a0-de17-339f-a7b6-2ca8c387817f | -6.08885 | -55.56816 | 2026-09-23 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 679c79c7-1adc-37f7-a55e-80cbe4a295a4 | -6.81268 | -59.43397 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6491e221-15dd-3354-80a4-92cd9192d027 | -6.92334 | -62.90352 | 2026-09-23 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ee7ddde-b0cf-3839-98be-1f50f49f2bfc | -6.67879 | -58.56039 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a885db08-aad0-37cd-b8f2-f4416c631393 | -7.31628 | -55.22162 | 2026-09-23 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8237649f-e579-321b-8b65-b5a90d59d7c8 | -6.10232 | -57.71087 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03dcd13e-531b-3b82-a8c1-02253bb02d91 | -6.88393 | -59.86161 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5f58f4c-6cbd-3834-a3b1-b9f1fcc3ff77 | -13.92857 | -47.8379 | 2026-09-23 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb76be04-9d96-37a5-a604-758b59dd7f96 | -8.46191 | -51.48438 | 2026-09-23 05:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eac9c3b-f06a-394b-a9d2-f7c5890d1bdf | -6.62094 | -59.93383 | 2026-09-23 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| da60f302-1c52-3582-a7ed-c88fd7cf78e4 | -6.62281 | -58.37571 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a6ea8b8-b500-3626-a4cd-7507f4b91f28 | -7.29088 | -59.52442 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f0d863b-32c3-30db-89f5-4d5a729f1b36 | -8.89915 | -45.95494 | 2026-09-23 05:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04fdcd15-cc2c-3b35-a69a-f5e7f4658c5b | -7.61549 | -50.42015 | 2026-09-23 05:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c9477211-b97d-37b6-869e-2acb03ed35da | -6.88061 | -59.86108 | 2026-09-23 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7d6c2a7-4bf6-3696-98bf-886c4c55afe8 | -6.29651 | -57.74804 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa616560-5092-378d-b453-5e1e31c87dc6 | -12.14402 | -61.17477 | 2026-09-23 05:25:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f451c5f8-1083-3dc5-9f66-4789728ad8d6 | -6.07204 | -57.72818 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24fd2aa1-0956-324c-9b31-ea1fb91e205f | -6.67275 | -55.07834 | 2026-09-23 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f8ab235-a535-3333-9ada-47edcb09409e | -6.67215 | -58.55935 | 2026-09-23 05:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd4763e0-501b-36f2-8d6f-335b06b0ad31 | -6.06708 | -57.8043 | 2026-09-23 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb400340-03b1-3645-bc9c-542a151c29c8 | -6.317 | -60.04734 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da61a18b-21b0-384b-9140-e946bb71f366 | -6.45549 | -59.96901 | 2026-09-23 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README115.md)
