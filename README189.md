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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c4e872-61f9-3772-8e49-eb67a270ea60 | -28.29065 | -49.42073 | 2024-10-25 17:09:00 | NPP-375 | ORLEANS | SANTA CATARINA | Brasil | 4211702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 64420b5c-9967-3b2f-80d5-c42253750ce2 | -29.4874 | -51.95459 | 2024-10-25 17:09:00 | NPP-375 | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 71cd8c05-57cd-3e34-bde7-d799865cee2d | -25.21984 | -53.97448 | 2024-10-25 17:09:00 | NPP-375 | MATELÂNDIA | PARANÁ | Brasil | 4115606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2039fb52-96b7-3b5b-97cd-2f9f06528cb4 | -27.13168 | -52.9422 | 2024-10-25 17:09:00 | NPP-375 | CAXAMBU DO SUL | SANTA CATARINA | Brasil | 4204103 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1d55eae2-1f7d-3ae6-933f-0bf99790e524 | -23.8513 | -55.32771 | 2024-10-25 17:09:00 | NPP-375 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 39.6 |
| 9fe88472-92b1-3437-9123-374fb3f96ddd | -23.8243 | -55.31449 | 2024-10-25 17:09:00 | NPP-375 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 277e57be-edaa-31d8-a0b8-2371736a83e6 | -23.82077 | -55.31504 | 2024-10-25 17:09:00 | NPP-375 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| b178953a-f84a-3cf3-bdd0-ee2dc34ab33d | -19.09308 | -40.99239 | 2024-10-25 17:11:00 | NPP-375 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| cd82be2f-c941-3ff3-94b4-ccfc58456653 | -19.0926 | -40.99244 | 2024-10-25 17:11:00 | NPP-375 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1660d7a1-907e-3efd-9888-7b9499bb3bcf | -18.71423 | -43.80468 | 2024-10-25 17:11:00 | NPP-375 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1caca9a-8188-34a8-91b0-66c8497e407c | -18.69354 | -44.14618 | 2024-10-25 17:11:00 | NPP-375 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 605df29f-5a04-3b8a-a4aa-5e45d2cdf6e8 | -21.4744 | -50.49949 | 2024-10-25 17:11:00 | NPP-375 | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 11c115b6-e0f9-3bfe-8f67-30291082ee47 | -20.24227 | -53.07031 | 2024-10-25 17:11:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 364ab327-2fe0-3a12-804c-573b08fba9b5 | -20.2417 | -53.06661 | 2024-10-25 17:11:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e79aabc4-35d6-39a3-af84-a6b07b0476a3 | -20.23894 | -53.07089 | 2024-10-25 17:11:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e472deef-14fa-3854-bf29-6b924e8d4ad7 | -20.23837 | -53.06719 | 2024-10-25 17:11:00 | NPP-375 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f463e46-b638-390b-b801-9e7e8603b4c5 | -20.83426 | -54.70016 | 2024-10-25 17:11:00 | NPP-375 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16682549-de60-35b4-b83c-3b1d93c887dd | -22.14185 | -56.57571 | 2024-10-25 17:11:00 | NPP-375 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c71ef74f-e1ff-3ffa-8bb7-93580f9a42f9 | -20.99336 | -57.72583 | 2024-10-25 17:11:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dee680c4-e5d0-3d37-b87f-d6b05974f502 | -20.98952 | -57.72639 | 2024-10-25 17:11:00 | NPP-375 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 96733e1f-24f0-3a73-9e8e-0d5f3daeeb54 | -17.2344 | -57.4926 | 2024-10-25 17:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.1 |
| d125afce-ad3e-3ac9-91e7-dd2b336a0588 | -19.526 | -56.7221 | 2024-10-25 17:16:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 0c060e61-9b58-3b5d-8e31-3368120ef9d7 | -19.5669 | -56.6744 | 2024-10-25 17:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| cf7b7e4c-f44b-3b26-8af9-9ac00ba18905 | 2.33146 | -50.77776 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 15c1a43e-af09-3287-b9ae-68bf8b466c75 | 3.7686 | -51.83374 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be868cff-14ff-3ecf-a452-26fba59df742 | 3.74266 | -51.77914 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7f080d58-0ff5-3d35-8592-bdaee2c9f04f | 3.7418 | -51.7806 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6713b988-d6e6-3f42-b4c8-0719704672d3 | 3.7167 | -51.5213 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c11ee54b-695f-3d56-92d6-4df7ff4763ed | 3.69972 | -51.37743 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f9f8f266-a336-3c5f-ba98-4dabe6dbda7b | 3.69767 | -51.37865 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3ac11abe-4aca-39ea-ad3c-b689d84270a4 | 3.69486 | -51.37674 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0fc1e47d-d3e6-3d8d-b5e2-dc0cab9b6f60 | 3.64328 | -51.28747 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 3d20f327-8934-3e72-9f51-09fe10707245 | 3.6376 | -51.29219 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a8ae927-7f04-3077-9b98-d82ae9ee77d6 | 3.56809 | -51.40981 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 28380fce-daa3-3213-a405-2ed2d089bd72 | 3.56646 | -51.40745 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6ca1308c-0169-3624-bd46-4d7affd1df52 | 3.46285 | -51.26178 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a9921d2d-0fc7-37ca-b8c4-0f8e977c9dac | 3.45796 | -51.2611 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 641287e3-ddb6-3cc9-a78b-cc00d5ed04c8 | 3.43116 | -51.27381 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c4a34ee-63c6-34b4-a01b-35df71b0a55e | 3.43038 | -51.27914 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bc99313a-a999-353e-a86f-72955bf537f1 | 3.42726 | -51.30056 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 17189ee3-2680-3a22-9e89-c106e8c8ce34 | 3.42648 | -51.30591 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 266bfd9d-7a63-3765-b025-c63c0e880774 | 3.42628 | -51.27312 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 393592da-35e8-3100-8aff-cb817f6405ec | 3.42161 | -51.30521 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7de3e631-6869-3dae-817a-25142408d85f | 3.41829 | -51.29384 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 83f83ae2-a994-31d7-87fb-a251e6a7dafd | 3.41341 | -51.29316 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fac20ab7-d25d-342c-b83f-1dde05804ddd | 3.41264 | -51.29851 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ca911e2-7c0b-3db0-b606-21162a8b2d94 | 3.38148 | -51.29095 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 2df367bc-ec99-3a9e-860d-dbd68ebcefdc | 3.37853 | -51.29368 | 2024-10-25 17:17:00 | NPP-375 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| eea90519-caf5-39c2-b18b-af57a3cabffd | 2.79847 | -50.93074 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 37b4b1be-2860-3654-bea4-55931af60c4e | 2.79742 | -50.93303 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c74feec0-1c7a-38b3-bf66-c69419f1e582 | 2.79351 | -50.93003 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 788ab977-30ae-3a53-93b5-16d239549ab5 | 2.79247 | -50.93232 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| eb8d3dcf-3455-37d2-9a84-2c1e34f64cb9 | 2.51131 | -51.0761 | 2024-10-25 17:17:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19f80a95-e679-37b7-987a-7e1d80dd3635 | 1.58205 | -55.65414 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae058edf-20dc-3433-a378-69c446048efe | 1.58144 | -55.65821 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b8382824-90c0-341e-a125-8b45481cee20 | 1.57189 | -55.64848 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 35112032-f7fd-3fd1-b0e8-347fa4ee69d7 | 1.5683 | -55.64795 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 203631dd-1470-3a7c-9aa2-fc45f903026c | 1.56532 | -55.64333 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ecd12376-dc59-38df-8bc4-e4e0fd490bf6 | 1.55754 | -55.64634 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6157168-a5ec-3350-819d-b51f3c520515 | 1.55395 | -55.6458 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cde46fd4-9fdc-3a16-961a-fba1a65609b3 | 1.55334 | -55.64988 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b09a27c0-56c6-31e8-b1cb-55b50d65ab7d | 1.55274 | -55.65396 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b1ae99f-80ef-39cd-a623-68dff1d95554 | 2.30232 | -55.93913 | 2024-10-25 17:17:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ee9fdbb6-d557-3677-a8c3-5c6af213bb9f | 2.07725 | -55.8782 | 2024-10-25 17:17:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 092bae9b-e63a-35d1-8808-21d416ec42a7 | 2.26923 | -59.80497 | 2024-10-25 17:17:00 | NPP-375 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.4 |
| bb545396-0e1a-358d-91cf-10394d5a1fa4 | 1.30067 | -60.41365 | 2024-10-25 17:17:00 | NPP-375 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a808b38a-75ba-3876-85df-bd9592f237ab | 4.34519 | -59.93481 | 2024-10-25 17:17:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b06018ff-f0be-35b2-8b8c-945a04556b6c | 4.19218 | -60.77856 | 2024-10-25 17:17:00 | NPP-375 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9f04210f-0c04-389b-816b-b7e04b569613 | 4.18878 | -60.77805 | 2024-10-25 17:17:00 | NPP-375 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9d98967f-e157-38a8-8bf4-ec6083d889f0 | 4.1075 | -60.31273 | 2024-10-25 17:17:00 | NPP-375 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eee0c14d-6a31-3ee3-a13e-72170e7b5218 | 3.68773 | -61.38561 | 2024-10-25 17:17:00 | NPP-375 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 30bce193-f85f-3a06-a2cb-cde5af68addb | 3.55822 | -60.38794 | 2024-10-25 17:17:00 | NPP-375 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab44a089-af37-34f8-8c87-20272edabf99 | 1.90602 | -60.37776 | 2024-10-25 17:17:00 | NPP-375 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25afe464-d59e-3b0e-9c4f-cd9ed485a1cf | 4.97755 | -60.06557 | 2024-10-25 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3d9b6346-dcec-34f7-92ab-42182964fc84 | 4.97702 | -60.06907 | 2024-10-25 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb397674-a33e-35fd-a752-fc9812607849 | 4.97316 | -60.07205 | 2024-10-25 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20f97464-bc70-3cac-a4b2-a43071ff31f9 | 4.95969 | -60.04856 | 2024-10-25 17:20:00 | NPP-375 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0d68861e-155d-38ed-b07b-a5c513dd44d6 | 4.74138 | -60.70256 | 2024-10-25 17:20:00 | NPP-375 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a96f354-6658-36c7-8ea8-09ae8482deea | -6.7666 | -59.1129 | 2024-10-25 17:25:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e49122df-2a67-3956-b6af-0ae12299b4cb | -19.526 | -56.7221 | 2024-10-25 17:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| eac0aaad-3178-3f64-a68f-62da80f37140 | -19.5461 | -56.7192 | 2024-10-25 17:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 728407c3-b0b6-317e-a450-b9de9418be7f | -19.5669 | -56.6744 | 2024-10-25 17:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 9b526bca-6ca7-3b11-a818-dc6d8097a299 | -19.5666 | -56.6954 | 2024-10-25 17:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| eb3b58cb-4eb1-353e-b18b-3a33c14f3bfa | -6.2744 | -47.8253 | 2024-10-25 17:35:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 524.6 |
| e85059b1-6400-3a42-9098-50526c591b51 | -6.5266 | -62.9483 | 2024-10-25 17:35:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| e22ea1c9-c07a-347c-8687-ab4c8c09a8a1 | -9.2701 | -45.2342 | 2024-10-25 17:35:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 094bbc51-2588-3f1d-8f84-444bf4288e78 | -12.9553 | -43.2091 | 2024-10-25 17:36:18 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 6aa6adac-1d43-3d85-a4e0-63f323ade0b3 | -19.5461 | -56.7192 | 2024-10-25 17:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 6fa44427-8e77-348e-b3d2-d2c48ee202d6 | -19.526 | -56.7221 | 2024-10-25 17:36:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.3 |
| 95006b27-fc01-30fd-8c44-7e7bcb137348 | -19.5666 | -56.6954 | 2024-10-25 17:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 315a6833-4c24-3c81-8778-80df58d0c48f | -19.5862 | -56.7136 | 2024-10-25 17:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 6143a506-ca77-3d09-af39-1c83415f8ccd | -19.5669 | -56.6744 | 2024-10-25 17:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| dadb7367-2f93-3019-b3f9-d3dfc8842902 | -19.5874 | -56.6506 | 2024-10-25 17:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.9 |
| b55eda1b-c25f-384b-9710-b0e37d025fde | -1.5878 | -53.3089 | 2024-10-25 17:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ea34ff53-52ce-357d-9c59-50fffe1191cf | -3.1116 | -53.7234 | 2024-10-25 17:45:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| 997eb14e-074b-3044-baff-e265a882b0c4 | -5.8961 | -44.16 | 2024-10-25 17:45:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 640fe9b0-0793-3a88-9164-4ae9ebb9548d | -6.5219 | -60.0457 | 2024-10-25 17:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2f41e6ee-d9d3-3dbd-8af0-5d23fd834544 | -9.2701 | -45.2342 | 2024-10-25 17:45:57 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3bd7db0e-5f4a-3bd4-9d0e-e13336eea83d | -9.6156 | -47.5962 | 2024-10-25 17:46:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 852c76db-c66f-3fe9-964f-b6d2a11b7330 | -12.8976 | -43.1953 | 2024-10-25 17:46:17 | GOES-16 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |


[Clique aqui para ver as próximas entradas](README190.md)
