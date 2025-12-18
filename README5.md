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
| 098daaa2-cb1a-362b-82f2-0d98ba74ab3c | -14.38869 | -43.97145 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20eecc51-2752-3457-ac48-9bb28682e123 | -16.64972 | -49.2784 | 2025-12-18 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bfa80996-a5d8-39e4-bdbe-51c10392722a | -14.39315 | -43.96487 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68f97fbd-818c-3106-86b2-165acc917e93 | -14.39144 | -43.97557 | 2025-12-18 04:10:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09fa23c8-b7d3-3453-b7ed-35c396837403 | -13.37946 | -44.37361 | 2025-12-18 04:10:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c813aca-b828-3eb5-afc8-1b946a12ee70 | -11.76198 | -43.31481 | 2025-12-18 04:10:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02214685-ee75-33d2-85cb-7d52f58cadb5 | -21.2003 | -56.93555 | 2025-12-18 04:12:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5de69bb-f721-3720-8ade-b570c03c5962 | -20.1967 | -54.77104 | 2025-12-18 04:12:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae205e92-0a38-3222-82cd-8c4ae3f76943 | -20.8751 | -50.07649 | 2025-12-18 04:12:00 | NOAA-20 | MONÇÕES | SÃO PAULO | Brasil | 3531001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6f634af8-9310-39be-add0-391ea798e4eb | -22.61401 | -43.7976 | 2025-12-18 04:12:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a923e78-bc90-3b7b-9932-ce20a5054875 | -16.04092 | -57.26091 | 2025-12-18 04:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d9fbac2-4f37-389b-a7e8-5c0d2bef4f71 | -20.19748 | -54.76745 | 2025-12-18 04:12:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0292c253-eb06-3db8-996f-6d617f084fab | -22.98178 | -48.64527 | 2025-12-18 04:12:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bbad3043-edb2-33b8-b4dc-858344028e8e | -18.38749 | -51.44774 | 2025-12-18 04:12:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8475578b-2fb1-38fc-802b-f1de449a8785 | -21.19442 | -56.93387 | 2025-12-18 04:12:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 583b664e-6d21-3835-bf74-89f752660d61 | -19.56303 | -50.99166 | 2025-12-18 04:12:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cf5e1c7e-5fab-35dc-b9e8-1c0f38f99c97 | -16.03955 | -57.2669 | 2025-12-18 04:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a18c85d2-7557-386f-a26c-6302a6652317 | -16.03696 | -57.26598 | 2025-12-18 04:12:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f713945-7e80-3fdb-8cbd-c6eef9c0e53c | -22.98101 | -48.64962 | 2025-12-18 04:12:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95e4f73b-4673-33a5-82b7-2605d4303a69 | -23.60807 | -48.34735 | 2025-12-18 04:14:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e1bd53-88f9-3bb9-ba20-0fd68117331a | -23.75615 | -47.41642 | 2025-12-18 04:14:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5608b7b9-2506-3cf0-a778-6ce5c5b1598e | -26.23409 | -50.36839 | 2025-12-18 04:14:00 | NOAA-20 | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7493e94b-9fab-3837-890f-fffeed09241f | -29.88143 | -51.21565 | 2025-12-18 04:14:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8766d43a-f90f-3835-bff7-2dd9e49e3d0a | -27.13462 | -51.20705 | 2025-12-18 04:14:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c478f6d8-c011-3eb9-9b31-881ec491a593 | -27.13326 | -51.20847 | 2025-12-18 04:14:00 | NOAA-20 | TANGARÁ | SANTA CATARINA | Brasil | 4217907 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8ae4ea55-74e0-3d6d-81bc-43ad85156544 | -31.25519 | -51.03426 | 2025-12-18 04:16:00 | NOAA-20 | TAVARES | RIO GRANDE DO SUL | Brasil | 4321352 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| ea30d525-4b45-30ed-bb57-5e1aa145582d | -32.35534 | -52.37385 | 2025-12-18 04:16:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| 290b94b8-430c-3706-9fd9-ae16259230e4 | -32.35901 | -52.37484 | 2025-12-18 04:16:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 9.9 |
| 834f47a5-e756-3875-acc5-ddcefa7f845d | -33.63676 | -53.45592 | 2025-12-18 04:16:00 | NOAA-20 | CHUÍ | RIO GRANDE DO SUL | Brasil | 4305439 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 2ea05174-2f14-30ed-b711-f69284ba423e | -32.35632 | -52.36872 | 2025-12-18 04:16:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| a93af5b4-f3e1-3ccb-af37-feb62082700f | -32.35166 | -52.37286 | 2025-12-18 04:16:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 10.4 |
| cf687f63-8566-36fb-a4f4-b931700a5dce | -2.20764 | -46.59804 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42f7af88-4d38-3c74-8324-cb29c7dc03fe | -2.2056 | -46.6117 | 2025-12-18 04:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de12a35c-2527-3aaf-bd56-41e8839726fe | -1.10589 | -47.33968 | 2025-12-18 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79d102b1-be19-3c79-b31e-dc63f12f7b3f | -1.51787 | -47.3643 | 2025-12-18 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3be1138-3100-3889-8273-b8149ecb2004 | -1.40496 | -51.73722 | 2025-12-18 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93942a8e-c48a-3796-a30e-2a9604431eb0 | -2.19723 | -46.60579 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b032f35-1649-3047-ac4c-985f09acfd7a | -2.21081 | -46.60783 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 705ceb66-c886-38f7-8998-2f8ee55fbc50 | -2.20695 | -46.60265 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5725d20b-181c-3aff-bd3a-bf6086a535a1 | -1.40777 | -51.74132 | 2025-12-18 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e29c7647-ccad-35bd-8e15-c7e6a0fc12a3 | -1.40833 | -51.73775 | 2025-12-18 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db23b435-0da1-3405-a6ba-64f213d65a5b | -0.79402 | -47.11766 | 2025-12-18 04:55:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88518f82-7ecb-3325-a1d7-f84d09669ffd | -2.21217 | -46.5987 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0d35dd8-3865-375e-adc1-544caa3269f9 | -2.21014 | -46.61231 | 2025-12-18 04:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d2f5ccc-bdc0-3361-9504-ee54da8baf77 | -1.12562 | -47.73924 | 2025-12-18 04:55:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33a28b07-83f6-390c-8e4f-f7bf6e178c7e | -2.20243 | -46.60196 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4be31f4-e8f6-3653-80c9-2bc6fc2af5e6 | 0.79023 | -51.96774 | 2025-12-18 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d28c5a6f-168e-375d-962c-3d6429ee4689 | 0.01272 | -51.12497 | 2025-12-18 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8673cadf-2337-3866-86c3-cdfdb15190c3 | -2.20175 | -46.60652 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80a55c84-6737-3152-8529-6e527347e300 | -1.52149 | -47.36897 | 2025-12-18 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6df2a5d-13f3-3c4d-9296-d61dc2d99e66 | -2.21148 | -46.60331 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb800c65-0227-3354-bd64-eef71c415153 | -1.18164 | -52.08265 | 2025-12-18 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 14381553-4b43-39e0-9ae8-638a606415c1 | -1.10543 | -47.34124 | 2025-12-18 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f068842-9bda-3e2b-a6dd-44df0007675e | -2.20108 | -46.61101 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b27f72e-1b54-3dd8-b466-7cfa5f20eeba | -1.40441 | -51.7408 | 2025-12-18 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3981acdb-3f8d-34dd-9c72-3fbda709d3f7 | -1.52212 | -47.36496 | 2025-12-18 04:55:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2800f5-d14c-35be-84f9-82dd987f6874 | -1.31506 | -51.7491 | 2025-12-18 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ba0d5d4-f4cf-319b-962f-1ddd0a78dbb2 | -1.04022 | -47.23017 | 2025-12-18 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d08f6f7-d835-3cd6-9834-c45c9afbde13 | -2.20628 | -46.60719 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa5e716d-1a38-3852-b960-2eeae268c862 | -0.79829 | -47.11833 | 2025-12-18 04:55:00 | NOAA-21 | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e592a57d-f8f5-3434-bd1f-2e1665f77e72 | -1.17831 | -52.08213 | 2025-12-18 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f844ff3-b8a1-324f-b735-2f4c801c54b6 | -2.20312 | -46.59734 | 2025-12-18 04:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59a99af8-d9b2-3cb7-a65a-dd885986cf25 | -1.74374 | -47.19188 | 2025-12-18 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc66b2bc-e198-387e-8b5b-7bec9a213a80 | -0.89835 | -47.99598 | 2025-12-18 04:55:00 | NOAA-21 | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77f21b41-0543-3234-9813-f90093f08eb3 | -2.40146 | -49.39854 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eed79f94-7651-352b-863f-c73b91dc13bd | -3.6628 | -47.55108 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 605dede3-dac7-3062-a301-0f66b6b460ea | -3.18983 | -50.23055 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21c25cd3-5079-3246-8b1c-e3f0eebf0b87 | -3.65847 | -47.55041 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c87bf93-d314-3ec4-b965-2b5432a2bc2a | -8.10455 | -55.00659 | 2025-12-18 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d534cc30-d1b7-3a22-a9df-0a2433c3226f | -3.90041 | -50.30836 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7300fe90-fd03-3b07-85a8-34ce2444430c | -3.78844 | -47.74343 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1d470e7-f981-3dd4-a93d-dceae6071191 | -2.79241 | -51.40652 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c40d3b8-d696-3076-bae3-b5c539f39db2 | -4.00745 | -50.31903 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b6f87d-5317-37c6-8f8e-e50f15c98488 | -2.69966 | -51.64202 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8bd04914-d2f8-3fd3-bd3a-ac7380e500f6 | -2.93325 | -48.23003 | 2025-12-18 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b06e4595-fcb0-3d75-8602-812f5847da70 | -2.65089 | -51.73168 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937b3156-3fd0-3544-a1a3-904842ea50c8 | -2.41335 | -49.34687 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 554b92e7-5083-38da-b00c-d438556f30a0 | -2.68144 | -51.73636 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 097de6e4-deb0-3c95-a8e9-283e4c69bcdf | -2.8474 | -52.60989 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8263518f-e059-3bd7-ba95-89c65cf4ae50 | -3.78415 | -47.74282 | 2025-12-18 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c066401e-379b-3073-a200-7b0d144d656d | -2.37223 | -51.99176 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33567967-887c-3271-ba47-f06275484b3e | -3.31927 | -51.60701 | 2025-12-18 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2d436db-e964-3233-bb0f-702c48f0b873 | -2.47084 | -52.12331 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24f5f49b-35a0-30fa-821b-d32971162c10 | -2.99113 | -51.008 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81dd4e55-ffc2-36cf-8ffb-497d51bc43e7 | -2.98967 | -52.3739 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 617c9949-1455-3e22-a71e-4e47cad82f6a | -1.70868 | -52.62793 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94bdc58a-9208-3148-8884-496c8bf771d1 | -2.41783 | -49.34284 | 2025-12-18 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7b5cff-6632-371a-b222-9f70da83109d | -2.44759 | -49.02679 | 2025-12-18 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da339ba6-0001-370d-b4cc-c4b25f8f2d7c | -2.37713 | -51.91567 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 743b69db-0ce4-3a27-a699-127e6a5f820a | -1.66933 | -52.09375 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50f46037-ceaa-381c-9c55-2ebcb75c415d | -2.99022 | -52.37037 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6941d2cb-ee65-39c0-8a35-80cd5b86d360 | -2.93734 | -48.23068 | 2025-12-18 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 031ee9f2-c6bf-3e26-82f3-49d880d8e054 | -3.17069 | -53.02326 | 2025-12-18 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31432d4c-897d-3319-a006-b04282d27c8a | -4.01071 | -50.32207 | 2025-12-18 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ca686f-72db-370a-8e1d-460238cad187 | -2.97102 | -52.69005 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e7c13a0-0d00-3d22-a187-2c05e74051f6 | -1.92235 | -52.04211 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7718e1e-1a77-3f5b-9b2d-90a1420b5902 | -2.45091 | -51.98538 | 2025-12-18 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afee21b3-a5f4-355b-bd56-94566cfe3f65 | -3.30844 | -52.70703 | 2025-12-18 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a924549e-afee-30fb-a359-4c4b80b0bed5 | -2.79585 | -51.40705 | 2025-12-18 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1444f1a1-6514-357c-ac13-305f91e6cf64 | -2.60501 | -47.95461 | 2025-12-18 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README6.md)
