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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a66330e7-56d3-3fa3-9664-36c70c8a020d | -15.62957 | -52.74934 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f21a414a-1c5c-3dd6-89f3-5b049653c037 | -13.00692 | -56.91237 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf04b5b7-3ee8-39d6-8268-720ee80f7b5a | -19.11472 | -44.02621 | 2025-08-28 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 644a1cb9-9278-3043-aff1-8ff25cc98978 | -16.36481 | -43.79248 | 2025-08-28 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f064e6d2-012b-3596-a448-86b2fe707867 | -19.54071 | -49.51716 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99c91dd5-f910-360e-bdf9-c854a8056b69 | -21.03084 | -46.23396 | 2025-08-28 04:10:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 679d3e6f-6482-3f36-95b7-e3e0f33c8283 | -14.91126 | -47.31317 | 2025-08-28 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 334f6549-2a53-3a3d-b39e-5210c91d9b56 | -14.34393 | -53.352 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 15c654cd-198b-3793-88f1-cb2e991b0d7e | -21.6772 | -49.05766 | 2025-08-28 04:10:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb8fd958-a9ee-3edf-bff2-cc25140809cf | -17.75444 | -44.49622 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0027f14b-9887-3130-abe3-48e2ce7ba7ee | -17.9178 | -45.90788 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8b57aa-0044-3579-b950-1c4604db68b6 | -21.13703 | -45.90152 | 2025-08-28 04:10:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 08f93a1b-6346-333f-b291-54916b3c4115 | -20.09425 | -43.74649 | 2025-08-28 04:10:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e1d2c73d-7c4b-33cd-a088-5b480969a2b1 | -17.90426 | -44.2585 | 2025-08-28 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ce1bb95e-930c-3abd-a09e-1359e3bf3aaa | -20.56015 | -46.38304 | 2025-08-28 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 1562d090-9037-394e-8861-da4f8cace13a | -17.72696 | -45.53013 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4143aa5f-bc34-3a26-937f-271cee103ebe | -15.0748 | -48.64309 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a693b9-1e8d-3459-8fda-91f5be9e8b30 | -21.8944 | -43.31007 | 2025-08-28 04:10:00 | NOAA-20 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8d944177-6232-343d-87fd-3af386fa157b | -20.11243 | -44.33445 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f90b88eb-c701-35c5-94f6-dae285bfad99 | -15.09454 | -48.53441 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d132c28a-8f8b-3af3-b94f-a05c7225d6e3 | -17.90483 | -44.25488 | 2025-08-28 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87d59e5-1d8d-34fe-8f84-af3c5711e5e1 | -19.27367 | -45.12912 | 2025-08-28 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5871a96f-460b-31a2-8efb-c86ea4fcbb8f | -15.08565 | -48.51576 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f12281b7-7b89-34bc-bb8a-315f4ccd6f53 | -18.21057 | -45.56075 | 2025-08-28 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ecfb5ac-7964-332b-bae1-79eb183d19f9 | -18.13762 | -44.45833 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0fc30212-0b96-3c7c-b426-8ade8d6c22c1 | -19.97289 | -47.51809 | 2025-08-28 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b34a5ce-ef81-38fd-bc61-90b983a82593 | -19.88536 | -42.16182 | 2025-08-28 04:10:00 | NOAA-20 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eda20526-947f-3eba-96cb-e4cbdcc8ea72 | -15.1751 | -52.33027 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e749073e-6e72-3895-8c96-dab88f320373 | -18.37016 | -49.27334 | 2025-08-28 04:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a24a104-a389-39b1-894a-cee07ec397df | -19.27699 | -45.12972 | 2025-08-28 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2615c72e-55ca-36c8-b10a-e3773d940985 | -15.68018 | -52.76453 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20954e77-3784-3a3d-b143-116fa84cc5bb | -18.05978 | -45.17402 | 2025-08-28 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e5b8dbbd-e8cb-3ed8-aa57-dd457dedc444 | -15.66873 | -52.74102 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cc575db-4f54-3509-b5f5-02fbd5cf84f8 | -20.1179 | -44.34301 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26024af0-1eb4-3e10-9a64-c2d56d965481 | -14.36354 | -52.0933 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eb940f0-28d6-3986-a8a6-d0d2356008bd | -22.68022 | -44.42064 | 2025-08-28 04:10:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 349900bd-9191-3278-bdf0-3674934f79d6 | -19.11861 | -44.02312 | 2025-08-28 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ad7db829-7480-3c95-83fa-4f684da4ba7e | -18.95121 | -43.8334 | 2025-08-28 04:10:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5c3e639-4384-3b53-b9e8-d164844bbef8 | -20.70589 | -49.85833 | 2025-08-28 04:10:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8e318575-2b44-3bf4-9817-987962c87004 | -20.37313 | -46.18951 | 2025-08-28 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e489d48-d97b-3176-ba39-bea5f8225082 | -15.63336 | -52.75724 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0c20525-3289-3c14-a6a7-b661746d6e18 | -17.96336 | -43.99018 | 2025-08-28 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14a0b3fa-e950-36f9-879e-14491e814a06 | -19.8199 | -46.03564 | 2025-08-28 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4db66f95-af83-3cd3-bf76-2bdb47f1cf62 | -15.07946 | -48.64015 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72958555-554a-3b1b-8aa5-bb9921d9d0c6 | -18.88549 | -43.71082 | 2025-08-28 04:10:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda77a16-d723-3a68-b118-c9364f82ccb7 | -22.87303 | -42.78293 | 2025-08-28 04:10:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a28c7dc1-3695-384f-8b31-213e3f14187a | -19.67313 | -49.36791 | 2025-08-28 04:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bdfaa696-d914-3ea6-8518-5b802106813b | -19.82051 | -46.0319 | 2025-08-28 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff569707-be96-3d0f-9bae-578b2209fe4d | -14.33223 | -51.90837 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b46994b4-63cb-385c-9efa-10e4d67c5d2a | -20.27093 | -41.52447 | 2025-08-28 04:10:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6837ab15-6288-3951-b826-81ca76f90252 | -14.33244 | -51.90569 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cdba6ed-ebcb-3dc2-bd0b-b1cf827d2217 | -15.67508 | -52.73593 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8d16ac2-0f0f-3e13-8d72-fae6cb65ae2c | -20.43824 | -46.01467 | 2025-08-28 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3288521-2ac1-3737-9afd-57f7141971d5 | -20.30894 | -46.03368 | 2025-08-28 04:10:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0956c6b4-e934-3e6e-b106-252d71773b96 | -19.11529 | -44.02255 | 2025-08-28 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9cc41118-950e-3fea-b608-fd4e34471a8b | -15.68167 | -52.76451 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afb1d934-ded2-3e1e-a446-019c2b57a060 | -21.13764 | -45.89779 | 2025-08-28 04:10:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d291982d-94cc-3ce4-94d0-0bf75b2c02b6 | -15.62442 | -52.74829 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47e77242-2375-397f-9875-a6094b85bea0 | -17.81936 | -44.51499 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf9a4a96-d2d8-30f8-b7b8-89f6063c525d | -17.84094 | -47.73912 | 2025-08-28 04:10:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7af7b0aa-47ea-3eed-843c-4c0a013f4715 | -17.75502 | -44.49258 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d20043b6-3369-3b17-98bb-1f483cb8d9dd | -15.17438 | -52.33394 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c73e9451-2219-3ced-9c90-f7d8bae5b872 | -20.14979 | -47.37526 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e246f45-a5e5-38f9-a7f0-251bfc71a421 | -17.8446 | -47.73975 | 2025-08-28 04:10:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6dcba94-68b2-3f47-aa3f-3460b918d191 | -17.76007 | -44.48225 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8616ab-04cd-37df-977b-188bd5d415c0 | -15.17367 | -52.33759 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68623fb0-f744-3f7e-b917-53563a89a59f | -17.9177 | -45.90468 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fee72147-001a-3037-b7b4-2ababa62012c | -17.75617 | -44.48531 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 314c9807-3447-363f-8994-69ee3b9598fc | -19.67698 | -49.36877 | 2025-08-28 04:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a92e115-9f7b-36b4-a12a-b3d043df76fe | -17.75833 | -44.49315 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 172ce615-ba2f-30e8-b6dd-17d06cb1b914 | -19.7907 | -44.11001 | 2025-08-28 04:10:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1b687a0-0ed2-3090-becb-94e1a5d2a585 | -20.25312 | -42.01051 | 2025-08-28 04:10:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 574817ee-dc79-3eca-a6fc-89299e673504 | -15.21148 | -48.24295 | 2025-08-28 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac8f2434-f7b3-3a41-a140-8bf6db4ea067 | -17.75949 | -44.48587 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5c1f304-968b-396a-ac89-8ccf386fe48a | -19.06073 | -42.133 | 2025-08-28 04:10:00 | NOAA-20 | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d48577d2-d43e-3b9a-b595-5b03ac1cba6f | -18.78128 | -47.18402 | 2025-08-28 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8880e96b-5f49-3011-9614-29eb877c8e81 | -15.0968 | -48.61265 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84047007-e5db-3608-98c9-f60b7081afb5 | -15.07959 | -48.51325 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7a05125-3c49-38c7-8eb4-3af31f7f6a18 | -14.33167 | -51.91127 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bea21b98-4249-374a-83dc-d4190f660338 | -20.67752 | -47.07878 | 2025-08-28 04:10:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa0b67c-ca8e-327e-9ff4-e70657a1839c | -15.07864 | -48.50928 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f66aff41-6287-305f-a735-bbe804a8a52e | -14.26875 | -53.07125 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1285bd1c-98c3-37ee-9305-bee0812715ba | -17.77497 | -48.49939 | 2025-08-28 04:10:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7ca02a80-160b-3724-ae55-1e5936f3381b | -17.80904 | -44.51687 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db02c4d0-8349-3628-a404-7d2f79bb9ad5 | -18.03083 | -43.88243 | 2025-08-28 04:10:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c3427ea-e3ec-3993-b2ba-448ddf31413e | -16.88341 | -44.61142 | 2025-08-28 04:10:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b98ab0a2-f14d-35b1-86db-74c2c0879e00 | -22.16455 | -47.07458 | 2025-08-28 04:10:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 497fe8d9-c6ee-3038-9591-b9368f8912b4 | -18.21545 | -44.52357 | 2025-08-28 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87e3d284-dac2-358f-894b-3262356bfec3 | -13.0002 | -56.90389 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc6c3f4e-5be2-31c4-88cf-9a95f9ccf267 | -15.10551 | -48.56441 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1136611a-ccab-394a-bfb2-8d80adf29b3f | -16.95591 | -53.51974 | 2025-08-28 04:10:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a5ccf2d-4912-30af-8da8-5f011ed670d6 | -15.66938 | -52.73772 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1befbda-f7a3-306b-93b9-3b7293c35d35 | -17.7556 | -44.48894 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2b67bcf-27de-3b06-bbae-2008d33721f6 | -20.11197 | -44.31549 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b51b2923-0b30-3f82-9ad5-1fe3072c4202 | -17.76885 | -44.49123 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69d40cc0-ccae-387a-b302-0c15857f5b1d | -17.54638 | -46.61396 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48e5b673-aad7-319f-aa96-f7c0eb79e442 | -21.02414 | -46.23273 | 2025-08-28 04:10:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af0bdeae-63e5-3c6f-b1d9-71d67ebafd4c | -21.19894 | -50.48077 | 2025-08-28 04:10:00 | NOAA-20 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c1ee4fa-bee4-3710-8131-2ddce3f6c436 | -21.61094 | -49.70118 | 2025-08-28 04:10:00 | NOAA-20 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be867b4d-5218-3230-a6cb-94c0348b5a2d | -21.13059 | -44.21735 | 2025-08-28 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
