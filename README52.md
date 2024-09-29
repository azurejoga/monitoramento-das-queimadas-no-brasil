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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59caab2d-42d2-32b3-8b44-d8a377673b28 | -11.21796 | -53.8732 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4542575f-1ee4-3e61-99a4-f3ee6ab33d35 | -11.21741 | -53.87671 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cd4bd31-b609-371e-8a59-ed157528847f | -11.21685 | -53.88022 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d64967e9-9889-351a-a9bd-54ee1382c253 | -11.2152 | -53.86916 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f687baf-34ea-3eb7-9fb7-1e9f60db068f | -11.21465 | -53.87266 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d2aa242-b66d-3c54-badc-ac5dd5db8dc4 | -11.2141 | -53.87617 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45871602-6c68-3d39-b79b-0595f436b66f | -11.21354 | -53.87968 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cefc985-8c98-37e0-a8f7-b496f56685aa | -11.21189 | -53.86862 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cf58f42-a44c-3094-8dc2-642ef73381dd | -11.21134 | -53.87213 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81b44de1-b8dc-3dd0-9043-c12461d858dd | -11.21079 | -53.87563 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9490be70-5d64-3143-bdca-39e5b273503c | -11.21023 | -53.87914 | 2024-09-29 04:49:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c20320ee-ed79-3870-b84d-a3ff96f25e1c | -3.66387 | -53.81665 | 2024-09-29 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 474098d0-9c8a-3fc5-b799-4c49222e3ddf | -4.51746 | -54.86506 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4663b5a-3f74-334c-afad-330cad33f0b3 | -4.51682 | -54.86908 | 2024-09-29 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0057f404-4dab-3d4a-bb69-0679d7856a50 | -4.06396 | -54.10006 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9be2dad7-5224-3b2c-9b01-1225141dff0c | -4.04625 | -54.01245 | 2024-09-29 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2264867-60fc-37a1-a04f-e735b6664fca | -4.04566 | -54.01614 | 2024-09-29 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3063fffb-3330-3811-a6ce-0d9a21b91ef4 | -4.04506 | -54.01985 | 2024-09-29 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0395d889-9237-34dc-9485-3d7bb31767e0 | -4.04222 | -54.01563 | 2024-09-29 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05ed44e0-9acd-339d-8162-cfc19b687645 | -3.9938 | -54.14764 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ea71af2-a6f2-3aca-b627-3215de9d7c20 | -3.99034 | -54.14714 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71668f20-54d1-360a-8b41-e5daed656411 | -3.98973 | -54.15097 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc080216-f2ee-37a5-94bd-9f104ca8a87d | -3.87271 | -54.34845 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c61d0dd-611f-3949-92df-4c856cdbae4d | -3.87209 | -54.35229 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1467c04b-b168-3878-ba8a-1c46933b62c3 | -3.74844 | -54.53297 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc0581c4-1789-3492-bccb-1c539d478e51 | -3.7478 | -54.53693 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 92cfe9a0-51c1-3205-bdb2-1d620c986c95 | -3.62642 | -54.5265 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bc297aa-9b57-3f2d-b3e8-f533ce57637e | -3.6229 | -54.52592 | 2024-09-29 04:49:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e17f0f2e-d5d6-3f38-b9d8-766561787d48 | -6.22047 | -55.645 | 2024-09-29 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7610ecd-39dd-351c-b0a3-95f8506e95fb | -8.0918 | -55.39066 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181822d7-cdbd-3c18-89a7-04bef55e2dbb | -8.09117 | -55.39454 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0e5a2cd-b81a-3b1c-ac96-50f1423a11fd | -8.08831 | -55.39008 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bf84deb-5a71-3ca2-a465-0d66864f723a | -8.08767 | -55.39396 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02b16fc6-fbc9-36b1-b443-1af5bcc90c1e | -8.08703 | -55.39785 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caa9f8dc-272d-36e2-a03f-6656c8709d8b | -8.08639 | -55.40176 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea3085a7-c2cb-3c8c-8bd6-d73f92e1458a | -8.08481 | -55.38949 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00786ebe-28f6-3d30-ab79-316a89c58e7b | -8.02195 | -55.70554 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b429ded-0dce-33dc-b340-423317a28045 | -8.02062 | -55.7136 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0907a582-2dc3-3075-a268-e7a54365470c | -8.01907 | -55.70091 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e39f5a6-e283-3fa1-a513-dde4e49aedb7 | -8.01841 | -55.70491 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3299654e-7033-3f47-8c07-49a76cfb924c | -8.01774 | -55.70894 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f3b2a17-099b-335d-b515-3c7a4ff8d3b8 | -8.01618 | -55.69635 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2d58ce-afee-3364-830c-0fc0d31d2b32 | -8.01552 | -55.70033 | 2024-09-29 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f7a37b2-921e-377d-9fab-7e0e923df728 | -9.7112 | -55.61527 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8d2c8db-2891-350d-b2dd-8505daa4d812 | -9.69302 | -55.50876 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b714e01-6083-3c75-9f67-44dcbaaee12f | -9.65883 | -55.58639 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26f3e083-a505-3937-9505-59384f0b8fc0 | -9.65601 | -55.58187 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15ea7af-5d51-3b13-b05b-d96c84db63ae | -9.65253 | -55.58133 | 2024-09-29 04:49:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b12123f8-7256-3fbd-bcc9-a6d45f4a6da2 | -3.58383 | -55.41508 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97406c3-2e58-3dd7-8336-6cc4c2c10e91 | -3.54481 | -55.4938 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f82a7f70-6d42-3253-b8b0-adbaa8a156b1 | -3.54412 | -55.49812 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dca12cd3-0b12-316f-96e3-7bad5395dc9c | -3.5411 | -55.49326 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74757e0f-0ae7-3fa8-98b4-3a50c86ce5a5 | -3.54041 | -55.49762 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8faabc4-7248-36e7-8887-ad4612bdc271 | -4.3144 | -55.73047 | 2024-09-29 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5510ec8-6e57-336f-ab69-e9461d4781c8 | -3.94902 | -55.5159 | 2024-09-29 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe1e7ffc-8545-35e6-bb36-e699cbbb8155 | -6.99624 | -56.59679 | 2024-09-29 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3975f544-b8be-3ffd-ac29-3bb0dd0c0650 | -9.89604 | -57.05959 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d546625a-e927-3230-89ab-8d8b57c2deef | -9.67305 | -56.95616 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0beb6709-5c72-3b24-8a12-1d8c57599901 | -9.6723 | -56.96062 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e18f17a-84be-3e0d-8ce0-b111f007a0ef | -9.67009 | -56.95109 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a880c0b6-7603-346f-aa29-b89446f8cdf0 | -9.66934 | -56.95552 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e597e90d-c3da-3ed5-a721-aa0db866d80f | -9.66859 | -56.96001 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15fab8d2-a603-326a-af7b-d703f5e30a95 | -9.66638 | -56.95046 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b22c3031-f788-317c-959b-bee96ba7bb08 | -9.66563 | -56.95491 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16796482-1473-3e1c-94ac-31e51d0f9d16 | -9.66487 | -56.95939 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1023d2c6-1f06-3d4d-8bc0-78fdfb639856 | -9.66192 | -56.95429 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bacd6e37-1d84-3fd3-ab71-e286e806f172 | -9.64044 | -56.95818 | 2024-09-29 04:49:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d97fe43-f3bf-3e35-9eac-d766a8235727 | -10.70454 | -57.22019 | 2024-09-29 04:49:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 882461c2-5f8b-3aed-92bf-d0bbc879c83b | -10.70378 | -57.22466 | 2024-09-29 04:49:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9f3c131-f9c1-321f-a117-c030b12e1392 | -3.7625 | -57.17894 | 2024-09-29 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811052ca-d21b-30c0-8273-cccc09f93d11 | -3.7584 | -57.17831 | 2024-09-29 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38376da7-2e30-3aa1-824d-8b1cb31d1358 | -9.8264 | -58.9694 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf6654e2-5907-3f41-af66-eb0ba0697d66 | -9.82574 | -58.97327 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbe26576-c4c2-3e62-a581-30f4bc3b515f | -9.82509 | -58.97709 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2452ceef-14ed-3fb5-8330-903991f469ed | -9.8229 | -58.96459 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e54dad-4e53-3ef7-a52b-4487e818603c | -9.82223 | -58.96856 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebebdcf7-b122-3374-b0be-d4378794b223 | -9.82156 | -58.97246 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8faa4770-f3b9-3c71-942a-f20c379c989d | -9.82091 | -58.97626 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 624def8d-53d1-3cc3-b1f7-bf6bb4ed7a32 | -9.81805 | -58.96775 | 2024-09-29 04:49:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7cef717-a373-3856-b152-83214dba29c6 | -9.67063 | -59.06823 | 2024-09-29 04:49:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5411fa42-9af5-35c9-be0b-782bd6089b63 | 2.30758 | -61.32557 | 2024-09-29 04:49:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b12663e-f06c-3ab9-bf5f-f386a6365307 | 2.30509 | -61.33055 | 2024-09-29 04:49:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c783cc-e851-343d-93ce-620fd2cc75d7 | 2.30449 | -61.32645 | 2024-09-29 04:49:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d545354-b3f0-339a-a5c6-c458a3014e36 | 2.30227 | -61.33077 | 2024-09-29 04:49:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71a5d784-9ef5-320c-9fbd-a2851ec7ed9e | -9.36499 | -67.42554 | 2024-09-29 04:51:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92f0fd25-0c9e-3d79-9171-6f441522bd80 | -19.20055 | -41.35369 | 2024-09-29 04:51:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 21928f42-9ca9-3790-a4e7-dd5c9aa9a612 | -19.19817 | -41.35273 | 2024-09-29 04:51:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3b3a03a1-03ed-31d5-8cef-75f8db9c2e19 | -18.54677 | -41.34617 | 2024-09-29 04:51:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c0d25a2e-2248-3e13-8325-cd53b96a9b6b | -18.54529 | -41.34206 | 2024-09-29 04:51:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0febc481-228b-3c7a-98d6-4dce4fe73b9a | -18.54473 | -41.3492 | 2024-09-29 04:51:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f3dfecf3-0f17-350f-acaa-358581b6e25f | -20.15701 | -41.6324 | 2024-09-29 04:51:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8c5f121b-9810-3673-9a1a-5ab45d7d1eb1 | -13.89698 | -41.66224 | 2024-09-29 04:51:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bf18f467-9cfb-3743-a9ac-c7cac5fefed9 | -13.89637 | -41.66786 | 2024-09-29 04:51:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4a67f76a-1101-3b38-9bdf-807aecc3c50c | -15.83668 | -42.1661 | 2024-09-29 04:51:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 0b15940d-5acc-3a53-802d-2add75982db1 | -15.8361 | -42.17184 | 2024-09-29 04:51:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| eb4877f7-34c0-3104-a3b0-c1e37e1af324 | -15.83016 | -42.16559 | 2024-09-29 04:51:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de618461-c9c1-376d-8e52-2d661eeeab3e | -18.8358 | -41.96712 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 706bbe89-7c9e-3f09-b38c-260ff7484cfd | -18.83378 | -41.96522 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| cc1c0db9-95ec-3329-a66d-9a9712103d4c | -18.83319 | -41.97174 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0ea5ffa5-f181-3096-92d3-aebb37bfbf45 | -18.82899 | -41.96672 | 2024-09-29 04:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |


[Clique aqui para ver as próximas entradas](README53.md)
