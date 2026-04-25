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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05b71ce8-dcc4-3e7b-b05b-67c9eae5522e | -23.08213 | -48.61762 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63442b57-1d4b-387c-829e-7a50932b6b9b | -24.66829 | -49.66843 | 2026-04-25 03:55:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6e76403c-7c5e-3296-b254-ab262484269c | -23.37527 | -53.61879 | 2026-04-25 03:55:00 | NPP-375D | ICARAÍMA | PARANÁ | Brasil | 4109906 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 80fffc6b-22ef-3517-aa52-aa0b6d21847b | -23.08335 | -48.61765 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37213457-99b9-3d89-9638-8a5f2aaae34b | -23.08408 | -48.61438 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84cf095f-1275-3fca-9819-77ff1fdc335d | -23.0366 | -48.43493 | 2026-04-25 03:55:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70335b87-ba13-3ff3-8661-31453a0d4bad | -24.67428 | -49.66654 | 2026-04-25 03:55:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91bcd8c6-7a62-3811-9672-8368f4e98674 | -23.07902 | -48.61297 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 054e2b90-63fa-3287-a0a2-e91b74d5456c | -24.66908 | -49.66496 | 2026-04-25 03:55:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cff40cda-04c3-382e-a14c-8f526266a373 | -23.08284 | -48.61434 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46075bc-f351-3bb2-b6fd-5f4c2697ac0e | -23.07777 | -48.61295 | 2026-04-25 03:55:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e01d56d-6896-33ec-8e65-90ffb91cdbba | -11.76909 | -43.64971 | 2026-04-25 04:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 063c52d8-1774-32f7-ab91-92c16de22707 | -10.55778 | -42.44761 | 2026-04-25 04:10:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f118729-e345-330d-a568-abb7374fb537 | -10.94729 | -48.83919 | 2026-04-25 04:10:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac0b714-41f9-3e07-b44d-b5ce276898f2 | -9.23204 | -46.65333 | 2026-04-25 04:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10b94b8e-9928-3cdf-9527-efa6acfd55c7 | -11.77737 | -43.66205 | 2026-04-25 04:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9609c7b1-4657-3db0-b9ee-614ed24c7855 | -10.94805 | -48.83497 | 2026-04-25 04:10:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c518f06-1ca3-3297-a81c-ad854181b578 | -11.77795 | -43.65849 | 2026-04-25 04:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b4bfea7-0f24-34a5-8bc6-eb193ffeb14d | -10.55833 | -42.44411 | 2026-04-25 04:10:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d612803b-d6ab-3a57-972b-ec2054f62435 | -13.37933 | -45.30324 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3720b9d9-52b2-3070-af20-75c69dc3a00b | -13.41449 | -44.31928 | 2026-04-25 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f26b570e-9e88-349c-b0b7-ced0d585355c | -13.41114 | -44.31872 | 2026-04-25 04:12:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5ef432b-4bba-357a-96ac-832540919d5c | -13.36899 | -45.30142 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60f9dfa5-a7ee-3b54-811c-898faf12512e | -13.37716 | -45.29491 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dc13c2e-39b3-3929-8043-b6b8414b4f16 | -13.98981 | -56.64528 | 2026-04-25 04:12:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d5521a-143f-3a47-9abd-d25332cb8084 | -13.37589 | -45.30263 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c6aaeb9-b770-3da2-bb59-0b92a661ad82 | -17.21597 | -44.30334 | 2026-04-25 04:12:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba4a3e88-2935-3b3e-a3c9-4bf094a5eb8e | -17.22317 | -44.30088 | 2026-04-25 04:12:00 | NOAA-20 | CLARO DOS POÇÕES | MINAS GERAIS | Brasil | 3116506 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2e22fd1-5cb8-3390-8a8e-8ca049264d67 | -15.86379 | -43.59969 | 2026-04-25 04:12:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2180cfff-87c6-328e-84b9-f05bdc071eff | -13.98842 | -56.65165 | 2026-04-25 04:12:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10c480f6-8612-3964-8985-0937ff916542 | -13.37244 | -45.30202 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dde57847-83e7-30db-872c-47008747ef3c | -13.36835 | -45.30529 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee40f978-8a00-3c1a-9210-eebe045b3144 | -13.18594 | -52.70642 | 2026-04-25 04:12:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5176192-34b1-3904-a61a-af9e5f305ce5 | -12.50597 | -46.67795 | 2026-04-25 04:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a356c9e-73f4-3b77-8e68-bac1580c1de6 | -13.37525 | -45.3065 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbe0acad-f964-33c2-8f73-d8cb862f7e43 | -13.37308 | -45.29816 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb734b6f-28ee-330d-ab48-680016286529 | -15.86048 | -43.59913 | 2026-04-25 04:12:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bfb0adc-cbd3-3b47-95db-c9d5ffba50f1 | -13.37652 | -45.29877 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d122398d-3fbb-3512-8483-2c97c31b9e42 | -13.3718 | -45.30589 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4855e67d-5b31-36b0-bc8d-cd7dfa40582d | -13.37869 | -45.3071 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e89734b-27b8-3bb1-a450-7fbefb6693bc | -13.37372 | -45.2943 | 2026-04-25 04:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d8d01cb-b398-34ea-867a-0b6e0c4d6f2b | -15.96577 | -51.36726 | 2026-04-25 04:12:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74f1b044-0368-3b2c-a27e-a4f482fe4416 | -20.15536 | -46.85456 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80c73666-135f-3c4e-ab80-ea7e8bd16ef9 | -21.08292 | -46.77102 | 2026-04-25 04:14:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2f4bf31-f6b6-320e-85ed-9707e4da36b8 | -18.50441 | -55.50163 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f69ce527-beec-38f8-a866-d9d5bcac3f64 | -20.87515 | -45.55008 | 2026-04-25 04:14:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16deba88-caed-3069-b6f8-2ea352bd1547 | -20.18077 | -46.89265 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e3a81c3-928b-3982-a4c5-fa47b6c6fc33 | -18.89328 | -39.92389 | 2026-04-25 04:14:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 46a2f1f1-8e83-34d0-b700-290ff33065ec | -18.50346 | -55.50595 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 33a35c45-520e-37da-8f3a-96ec29641497 | -22.83816 | -42.157 | 2026-04-25 04:14:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa9d49fb-3ce3-3f71-bd50-99a72e83cd4d | -20.25432 | -46.76741 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 291074d3-7d58-3452-bbd6-dbc0b9897d32 | -18.50195 | -55.50792 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 71ba6b55-25d1-3e31-85f7-7ea2a6e56983 | -20.18349 | -46.87656 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4158a75-0005-3efe-8837-755a4e024aa2 | -23.79852 | -47.52048 | 2026-04-25 04:14:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc22724c-2831-3810-85ca-ba42b03e4860 | -20.81219 | -45.18215 | 2026-04-25 04:14:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 57bd4b18-9176-30dd-a1f6-20b0cbcd8eef | -21.85936 | -46.97935 | 2026-04-25 04:14:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60cd7303-e66a-322a-8aed-5a7012741012 | -20.24409 | -46.76537 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87207fe8-c016-36fe-99cc-cd0acb3f3b37 | -20.35424 | -48.3434 | 2026-04-25 04:14:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a47da6f-8d97-34a7-bbb2-7e07240dc7a0 | -20.19679 | -46.79792 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f48fb2f-857b-347b-9651-efe11da64265 | -18.50924 | -55.50739 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| def63924-fd86-3939-a2a3-15b3e6e0ccee | -23.79842 | -47.52159 | 2026-04-25 04:14:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 21a1f3d2-1764-36e2-a047-88eec9158817 | -20.208 | -46.87271 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aed00965-8561-3e8d-a041-0618059472fb | -24.66746 | -49.66679 | 2026-04-25 04:14:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 62ac7326-c6a6-3640-8354-409bfdf48937 | -20.1869 | -46.87734 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 392cffa6-f04d-310c-845c-9bd9899019aa | -20.25154 | -46.76301 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d3c18ed-5327-31d5-b26d-b57ca90ed9d9 | -20.15876 | -46.85539 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86ca4edb-e661-3610-a180-a8d1ba8f7e17 | -20.18159 | -46.95073 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b20ea8d-926f-375a-a7b4-2bf8e99a725f | -22.9696 | -52.69513 | 2026-04-25 04:14:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| faaaca3e-09e5-3dcf-a304-7fd6ee402f11 | -20.16831 | -46.86171 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0baada5b-c987-3d80-8e3e-a5adb0fc7e07 | -23.08247 | -48.61257 | 2026-04-25 04:14:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2ba8f05-1e8e-3eb6-83f3-cc216f7ea500 | -20.03212 | -47.18891 | 2026-04-25 04:14:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8e9ed90-4dfa-31ae-9e4f-8fb44e8d2a66 | -20.19441 | -46.87481 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac2f4a11-4fcd-3e1b-ab6f-4d8b84939476 | -17.76567 | -49.2416 | 2026-04-25 04:14:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb606692-66ea-3e8a-8a49-c07c81c25457 | -23.4056 | -46.42196 | 2026-04-25 04:14:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 245ba2f7-94bb-3cc4-bb23-71b0386b1485 | -20.19032 | -46.87803 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 46096b53-65b3-31f8-a7f4-e850df7251ee | -18.51019 | -55.50304 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ed90e1a0-ebf2-34f2-9627-33328e511f57 | -23.03481 | -48.43279 | 2026-04-25 04:14:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b2c0ba2-142b-38aa-8d33-a440e3167489 | -21.1828 | -48.6309 | 2026-04-25 04:14:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 640f7ea6-1abb-3bfe-a556-99bd7a016ad5 | -20.18146 | -46.88857 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a96d8b8-6b83-3ba9-8199-d43c7bf15889 | -20.19376 | -46.87867 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8343013-dd5b-3fd8-8dad-71edcda27d49 | -20.48324 | -48.58667 | 2026-04-25 04:14:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5518644-1f80-367c-bb37-1d8a5499ba94 | -21.36313 | -48.67299 | 2026-04-25 04:14:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 750ee7a8-8584-35ec-b6b9-818a48f28fcc | -19.77085 | -50.72864 | 2026-04-25 04:14:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1157e3ec-48c5-35ad-be02-50af83d57634 | -20.16898 | -46.85778 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 9cdd065e-81f7-3e0c-bf43-3959c5d772e2 | -20.16787 | -46.92685 | 2026-04-25 04:14:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 336befe2-8e84-36b2-9b64-8c825d73a8e5 | -19.96104 | -44.70427 | 2026-04-25 04:14:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53486b2f-d2d2-38eb-914f-2954addc9480 | -20.67549 | -48.96308 | 2026-04-25 04:14:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15687d4f-76f6-3fe0-aa8e-f09eb74d8986 | -20.46387 | -45.57204 | 2026-04-25 04:14:00 | NOAA-20 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3033915-0b87-3bf0-868f-2e6d4ab13463 | -18.50292 | -55.5036 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d6271890-580a-3c80-b280-663eef29d003 | -24.6711 | -49.66765 | 2026-04-25 04:14:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ff43910-752f-3176-9f17-6cd0b3a85bd2 | -18.35086 | -50.37642 | 2026-04-25 04:14:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 452eee4f-37c6-3733-912c-a5e5a105f1d4 | -20.24814 | -46.76229 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38504dae-71ba-3a3a-877d-0773d7523abf | -20.67636 | -48.95829 | 2026-04-25 04:14:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8cf57010-aa60-3981-b978-9250562c81c1 | -24.67196 | -49.66298 | 2026-04-25 04:14:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9bc2de46-fd40-346e-b246-6da2980ebb48 | -20.16697 | -46.86955 | 2026-04-25 04:14:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3b41087-8fd7-35f0-90f0-dbc3b3a4bd08 | -20.17539 | -46.92441 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebc87254-6fcb-36d1-abee-d5ba65af0700 | -20.17472 | -46.92836 | 2026-04-25 04:14:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4dd20fa2-8a44-36b6-b92d-afe5b9fe2d7d | -21.86003 | -46.97544 | 2026-04-25 04:14:00 | NOAA-20 | VARGEM GRANDE DO SUL | SÃO PAULO | Brasil | 3556404 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7101e63c-fc3d-3bc1-9eab-9e63771aa68d | -18.50871 | -55.50502 | 2026-04-25 04:14:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cfeb6fae-9a19-34f0-803d-d2b03a283d12 | -20.62823 | -41.67926 | 2026-04-25 04:14:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
