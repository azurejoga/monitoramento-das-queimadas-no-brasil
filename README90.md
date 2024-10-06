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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6b115ab-2a27-38cf-a243-ad2c79bca7f9 | -18.67847 | -57.26957 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c3541655-7a35-3510-bddf-56e453f9d8eb | -18.67315 | -57.26829 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c04660f8-867b-32a6-88d0-70873d78b956 | -18.66859 | -57.26349 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 10342905-6e55-3b29-9cc6-0dd6d70b2dc7 | -18.66784 | -57.26703 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c1275f2a-7da9-3efe-87e9-f423a85083fd | -18.66252 | -57.26576 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 32446e77-6512-3d4f-ae8c-04bc52b9c8b1 | -18.66177 | -57.2693 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8d9b7386-abed-3875-b734-5825719f6d90 | -18.65721 | -57.2645 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 29fdfdb6-d3eb-31e7-bdc8-b37d68f018dd | -18.65645 | -57.26804 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f9d8671a-df33-3216-88c5-ad4506723f26 | -18.65189 | -57.26323 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 8c274ee3-bba2-33d8-9bfb-548beb9c19df | -18.65113 | -57.26677 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 62a267cd-9ee3-3ff2-ab93-5fc2c640cd97 | -18.6504 | -57.29638 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23c80db4-dd7c-3666-9829-8b4c650cea8d | -18.65038 | -57.27031 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 5c76ece3-ec42-311f-92fa-3b821d9a5d96 | -18.64962 | -57.27385 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7abf7518-17ba-31ff-8295-6d1fad1e6dde | -18.64507 | -57.29512 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 2a33661c-dfcb-3fe6-b0cb-2742d89111ba | -18.64506 | -57.26906 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 6199013b-d97a-3148-9696-84c66d320b50 | -18.64431 | -57.29867 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c318eb40-3249-35a4-9eae-fb0e39dd4ded | -18.6443 | -57.27259 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| ba935adf-dae6-372f-b18a-12f6a950bb33 | -18.64355 | -57.27612 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 30c527eb-d374-3f8f-a0dd-134383d943e3 | -18.64181 | -57.27122 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9d10d068-380a-30e9-8273-2ab411f2b73f | -18.64108 | -57.27477 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| bf3c07bc-ac2f-33d4-83a4-e3f23c4a8d61 | -18.64034 | -57.27832 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 6f970a75-7972-3b89-893b-9d30a9630765 | -18.63961 | -57.28186 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| b7326147-8928-37c2-aaee-5f75adfd29a0 | -18.63898 | -57.27132 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e437fdde-1065-3400-803a-c144ac8f8998 | -18.63887 | -57.28542 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| f10cf069-4540-3af3-a5c7-7574c3fb5a04 | -18.63823 | -57.27486 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d64a26d0-6da2-3702-891b-721346db9631 | -18.63747 | -57.27838 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 34ea9e30-6380-3d7a-867a-00f40c507594 | -18.63671 | -57.28193 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 792ac5fc-745b-3d43-b09a-62c3e00b7471 | -18.63594 | -57.28549 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| b40a4486-e549-35a7-bdad-85abc62b614a | -18.63575 | -57.27349 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| c6cedfdc-7e71-3754-a824-0945d11f9d20 | -18.63502 | -57.27702 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 7a54b8ea-2db3-3989-80cd-d52f9af3cd4e | -18.63428 | -57.28058 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| e727c6d2-dec3-3cf6-a335-3a216073e4ae | -18.63354 | -57.28415 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 14e6e50d-6ed2-3c6b-baf3-01957fdef8a5 | -18.63281 | -57.2877 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 161d08ef-a56d-3304-a83a-7157a3764b48 | -18.63214 | -57.27713 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| e4519939-ca65-35af-a05b-9de6a19fbdef | -18.63138 | -57.28067 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 2fe890ec-1786-3632-95a5-9edc3453f59e | -18.63062 | -57.28422 | 2024-10-06 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 0f409e98-6508-366c-acf9-0f61bb8aae1d | -18.33261 | -41.44785 | 2024-10-06 04:21:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 857df7a8-5d1e-3efb-98a2-693ed71e75f6 | -19.33458 | -40.87066 | 2024-10-06 04:21:00 | NOAA-20 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 742f30e9-2473-3721-b6ae-3de683aec5ba | -18.33313 | -41.4437 | 2024-10-06 04:21:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a18c8231-a954-3a30-bd3b-5d8a0d8006a7 | -18.32837 | -41.4474 | 2024-10-06 04:21:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca41368c-ed63-387e-86a9-2f4b1db9918f | -18.32468 | -41.44267 | 2024-10-06 04:21:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 99528469-8646-3f23-a17c-43cf763918cf | -18.32415 | -41.44682 | 2024-10-06 04:21:00 | NOAA-20 | PESCADOR | MINAS GERAIS | Brasil | 3150000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5df3229a-4737-36c6-ab32-09c1afb12d99 | -22.59645 | -42.21346 | 2024-10-06 04:21:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 693f6e6b-584d-3a18-bd1d-d1e3883fb400 | -20.89986 | -42.91764 | 2024-10-06 04:21:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10bf4be8-59a4-3ea2-8b3f-307f3cfc24ba | -20.14808 | -42.31966 | 2024-10-06 04:21:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 788e37e8-acb4-3b12-97bc-e2e36adee6be | -20.14761 | -42.32338 | 2024-10-06 04:21:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3937963d-bf23-3417-ac37-f0a935720efb | -17.64 | -44.42285 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 50623db9-d070-3c55-93ec-e2064b5a1ba4 | -17.63529 | -44.40496 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f38187-bdaa-3b00-8d42-76de087a75ff | -17.63353 | -44.41751 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19bac68f-07ae-3362-b50a-842c19587ed7 | -17.63294 | -44.42171 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d312fccb-91aa-33f9-87df-289c8fd02aec | -17.63176 | -44.40439 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 721638ca-90fe-38d7-8026-6580157927c3 | -17.63165 | -44.40538 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ea9451e-7f46-3952-80eb-67b002a9a48b | -17.63059 | -44.41274 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ad13c6-cb6c-3c73-9639-bc0c5f7b6d09 | -17.63044 | -44.41373 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5254c5a4-bf7d-39a6-ab30-1a2f7be488a2 | -17.62984 | -44.41791 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ddafbc0-040f-3b3a-ab10-860d26b63dec | -17.62942 | -44.42112 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a544f8b-6968-3c05-9d09-dd56c60237c5 | -17.62922 | -44.42209 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d80ab2b-f86b-3b5b-bf18-ce8a73fcc26d | -17.61926 | -44.41615 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a8ba922-d766-3ac3-838b-45d3d0400e94 | -17.61866 | -44.42031 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6acd00ea-49b7-3cb8-8a93-dca0344abbcd | -17.61574 | -44.41557 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4716a71b-5879-33cb-9fb2-441d364b5240 | -17.61514 | -44.41972 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57791fdd-dfde-3277-b6fe-17ce272386da | -17.61453 | -44.42388 | 2024-10-06 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a262f106-ad2f-3773-9f4f-25fd2fa92ecc | -17.5956 | -43.20041 | 2024-10-06 04:21:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a65744c7-70e0-359a-b7bf-beccc1651c1e | -19.38699 | -44.32191 | 2024-10-06 04:21:00 | NOAA-20 | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af9ad000-ca5e-3133-922b-fb5d981cb52b | -19.29328 | -43.78157 | 2024-10-06 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 512bec98-7e0d-3f98-8121-d666f3296fed | -19.03263 | -44.51443 | 2024-10-06 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368434e0-3db5-31ba-9618-9a2bfb09087c | -18.75385 | -44.18544 | 2024-10-06 04:21:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19ae548e-576b-35eb-965c-08d1632883b0 | -18.56379 | -43.83368 | 2024-10-06 04:21:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2dc90914-e31c-339d-9f2e-3b9fc8b38e9e | -18.56314 | -43.83833 | 2024-10-06 04:21:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d4ea7e0-cbfe-3c8f-bf60-984195f4fd51 | -19.8812 | -44.40776 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 338cc92f-081c-3bdd-8581-98c5c1cdd2d6 | -19.87819 | -44.40287 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e629cbaa-2ca7-37ae-b921-d2e3fdba62f9 | -19.87758 | -44.40721 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67554444-2dce-3e42-9204-9feef7f2311c | -19.81262 | -43.84677 | 2024-10-06 04:21:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a88607f-5341-33b0-817d-90ed8c7f190a | -19.77115 | -44.26107 | 2024-10-06 04:21:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4e974f26-dbf9-344d-86bf-a75513f40665 | -19.63122 | -44.11331 | 2024-10-06 04:21:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e08fd025-4330-3333-a9be-7d0b101e05a7 | -20.05117 | -44.06883 | 2024-10-06 04:21:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f5ec15f-4844-3ede-9599-27e93e5bb362 | -20.05033 | -44.06676 | 2024-10-06 04:21:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 004adcb8-7ded-3728-85f1-6ac57783c642 | -20.00942 | -44.48269 | 2024-10-06 04:21:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 30109357-3796-3c2c-9c78-3bd96c7a7e4b | -19.91831 | -44.51995 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 151a533f-403c-35e0-a8f7-cf47999064ea | -19.91772 | -44.52423 | 2024-10-06 04:21:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 0a91fd96-071e-3902-9b8c-eaf0173f45a3 | -19.91471 | -44.51936 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 922f491c-3136-3bd2-bbd6-733acb0b501f | -19.91112 | -44.51873 | 2024-10-06 04:21:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a46b2904-ff8a-3f6f-bf0a-d7e58d51e099 | -21.19414 | -44.9365 | 2024-10-06 04:21:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1122c99-6d67-3a68-8ea7-be765ea52557 | -17.81965 | -45.89971 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a990b1dd-76bc-3813-a84e-65fa9c3cedeb | -17.81908 | -45.90343 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b6d9d15-da98-3dd4-8a7a-d6d1d4614aa3 | -17.81628 | -45.89917 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf6db6f8-d2cb-3f54-a603-ab019e107586 | -17.81572 | -45.9029 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd7d5f54-1e28-3366-9345-10eb6c465c0b | -17.81516 | -45.90662 | 2024-10-06 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79599d27-17af-307d-908f-747b7f6a62ef | -17.5869 | -44.51548 | 2024-10-06 04:21:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5153b0a-9cbc-360b-a1de-7102d9c4ade7 | -19.29975 | -46.22466 | 2024-10-06 04:21:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1590694a-b673-379f-8d63-5f17833075e6 | -18.08295 | -45.61322 | 2024-10-06 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2c2b17b-9b20-35ef-b79e-2b33ca5fe08d | -20.76378 | -46.28458 | 2024-10-06 04:21:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fda7558-7eb3-30a0-8877-10b751398f3f | -20.76321 | -46.28844 | 2024-10-06 04:21:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2da44df-a4ea-32b3-9319-b07c0e8fd8fc | -20.74779 | -45.59892 | 2024-10-06 04:21:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d89eabd8-5250-3003-b5d3-183abb06b1c1 | -20.62102 | -45.82552 | 2024-10-06 04:21:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35385686-4589-3bbc-8259-7a5eee6d2c2e | -20.62044 | -45.82955 | 2024-10-06 04:21:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff19f0d0-1de8-30da-891a-da32a77f7e48 | -20.57579 | -45.82222 | 2024-10-06 04:21:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51af8d7e-376e-3814-afe9-cf5f9d54c943 | -20.26345 | -45.59589 | 2024-10-06 04:21:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ff7c5db-aad0-32e5-9007-fa5a7be465e2 | -20.26 | -45.59533 | 2024-10-06 04:21:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| deeba60f-d267-39c2-a50a-395d78d3b445 | -20.02441 | -45.65288 | 2024-10-06 04:21:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |


[Clique aqui para ver as próximas entradas](README91.md)
