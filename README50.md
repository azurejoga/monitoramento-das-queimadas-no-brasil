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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ad5b0a-5850-34e9-bd54-eb9fdfa71174 | -4.6371 | -42.4769 | 2024-11-19 12:40:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 418ee131-11d0-35be-8641-2d8b82d21d27 | -3.9483 | -41.9491 | 2024-11-19 12:40:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 175.2 |
| e393fb5d-327f-3acd-9147-68f383741d03 | -4.1246 | -43.5833 | 2024-11-19 12:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 289e4238-9a84-3afc-971a-9112608347ef | -4.1059 | -43.5843 | 2024-11-19 12:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| e8b28eeb-1f39-3d8f-ab5e-0eed601eae2f | -4.1059 | -43.5843 | 2024-11-19 13:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 0478cdfc-b492-3c41-82e5-2a591375f809 | -4.1057 | -43.6074 | 2024-11-19 13:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 90048692-dc61-3c3f-9ca4-b9878caa12ec | -4.6371 | -42.4769 | 2024-11-19 13:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 4bf57216-c1b4-31c9-a6e0-f0d3fc8e75fb | -7.8865 | -44.2134 | 2024-11-19 13:00:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 8bf39d93-bdcd-3a4a-8ce0-6496f34ef317 | -3.6809 | -42.8609 | 2024-11-19 13:10:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 10d59174-172e-3b5d-9dd4-6c08cf2f1125 | -7.8865 | -44.2134 | 2024-11-19 13:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 09aab1cb-9ace-33d8-9c9e-f7d55fe8271a | -4.6371 | -42.4769 | 2024-11-19 13:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| a281fa51-ccdf-3800-a909-d160fe5de8f3 | -7.9053 | -44.2115 | 2024-11-19 13:10:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 409188af-5278-3192-93e3-f46a038c8775 | -8.4339 | -44.1788 | 2024-11-19 13:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 3921cb1c-988e-3a5a-8ee0-405c9d6e1335 | -7.9053 | -44.2115 | 2024-11-19 13:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e52efa28-4470-359b-800f-ac532cd3a626 | -8.2665 | -43.9883 | 2024-11-19 13:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 7155236e-e8d9-3dba-87c6-745f445f628c | -0.8412 | -47.5389 | 2024-11-19 13:20:00 | GOES-16 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a1e99182-e40b-3f2b-b524-694157d09fc8 | -7.8865 | -44.2134 | 2024-11-19 13:20:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| 850e29f5-dfd3-381c-9c60-39eaf896c52f | -8.4336 | -44.2019 | 2024-11-19 13:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| b73cc8f1-f37a-3306-a18d-7e68a74ad034 | -8.2854 | -43.9863 | 2024-11-19 13:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 8c172795-6db7-3699-a594-ae5134ffc3cc | -4.6371 | -42.4769 | 2024-11-19 13:20:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| b5fdc5a6-41b7-3a76-b3e2-ee5518022137 | -3.9483 | -41.9491 | 2024-11-19 13:30:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 39da5d5d-bc4b-33b7-92be-7641ffd87c83 | -7.9053 | -44.2115 | 2024-11-19 13:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| b9a1dd8b-7e5a-3d85-9a52-2c4411223d71 | -7.8865 | -44.2134 | 2024-11-19 13:30:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 5d46ba82-6947-3bf2-8512-4761c0ef85ca | -4.6371 | -42.4769 | 2024-11-19 13:30:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 77872336-3b67-36d7-ad24-fa55ae2aaad1 | -4.39 | -43.0094 | 2024-11-19 13:40:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 42c16832-37ce-3b47-ac0c-ae707d27d7af | -3.5545 | -42.1126 | 2024-11-19 13:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| b3fd0155-7c0d-34d1-8736-eb5d65a5912f | -10.4009 | -44.4731 | 2024-11-19 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 5f3706a3-a6c6-337e-818d-0c5980bff51b | -3.9483 | -41.9491 | 2024-11-19 13:40:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| f0735b44-7221-3a31-89ae-4a9bfaadaa0c | -7.9053 | -44.2115 | 2024-11-19 13:40:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| ce7e2544-1cfb-3310-a782-13441efce683 | 1.5468 | -55.8846 | 2024-11-19 13:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 62bdd8d7-20e9-34b6-9b58-e5def6618d00 | -10.42 | -44.4705 | 2024-11-19 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| b585c6e3-3d5d-3b0d-8478-76f794ed7f42 | -10.4196 | -44.4937 | 2024-11-19 13:40:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| fb9b67d8-8878-31fb-9e5e-9a68f288d1b2 | -7.8865 | -44.2134 | 2024-11-19 13:40:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 164.8 |
| e8bff3ab-23c3-3db1-be7e-f1aea5b408e4 | -7.8862 | -44.2365 | 2024-11-19 13:40:00 | GOES-16 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| dd67ff02-d8bd-3761-88ef-92c48e91d322 | -8.4336 | -44.2019 | 2024-11-19 13:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| bab7ab8c-7984-369f-8fc3-8aa1ad040b5a | -3.9483 | -41.9491 | 2024-11-19 13:50:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 1139fe34-5895-3120-acba-8f1b1b32cf4f | -10.4009 | -44.4731 | 2024-11-19 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 0fc8f327-c77b-3066-83ab-4577291eefea | 1.5468 | -55.9043 | 2024-11-19 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5112d864-282d-3973-9023-fcd0c5efffdf | -8.4339 | -44.1788 | 2024-11-19 13:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 02dbbbda-a3fa-3839-9e20-4cec6b57de2f | 1.5468 | -55.8846 | 2024-11-19 13:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ca3ca6b8-0cff-355b-b93d-ca5eacaff797 | -10.42 | -44.4705 | 2024-11-19 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c909a264-7bfe-3d3c-b395-8f457bc14000 | -3.5547 | -42.0888 | 2024-11-19 13:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| d0cf360a-0def-3bcc-9468-15c724655a95 | -10.4196 | -44.4937 | 2024-11-19 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 514dbaea-f154-3b06-916a-570343a15398 | -10.4005 | -44.4963 | 2024-11-19 13:50:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 36b15bbf-570c-3ba2-8706-9676e84d9530 | -3.9477 | -42.0443 | 2024-11-19 14:00:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| e0a26828-6dbb-39b2-97a6-c2a6e4d44c8f | -8.4525 | -44.1999 | 2024-11-19 14:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 53527319-77b2-3765-80f3-cf31ddea2837 | -10.4009 | -44.4731 | 2024-11-19 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 5e194f08-e929-3f93-b9aa-299483c7d0c8 | -3.5547 | -42.0888 | 2024-11-19 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 104.6 |
| ef2e4f6b-9f90-3ee3-ae97-84805e6f355e | -8.4336 | -44.2019 | 2024-11-19 14:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 92dd0829-0b16-36e8-b91c-85b4db84e041 | -3.6489 | -41.9652 | 2024-11-19 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| dc2518ef-6c21-36b4-bf9f-0f92557a41f9 | -10.4005 | -44.4963 | 2024-11-19 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9d22bf77-440c-3aef-9ca6-db98c6f73de1 | -3.5174 | -42.0669 | 2024-11-19 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 40a7c1c4-5e4c-3c5a-80e7-92388812c348 | -10.4196 | -44.4937 | 2024-11-19 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 454b21d7-7a5f-35c1-b46a-aa3a40d6fc13 | -10.42 | -44.4705 | 2024-11-19 14:00:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| ac1c935f-3a5c-3365-9f51-54d9dbccd713 | -3.9483 | -41.9491 | 2024-11-19 14:00:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 30ec107d-9144-3018-8e77-979b09e1c952 | -3.7219 | -42.27 | 2024-11-19 14:10:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| f6fb66fc-b33d-3309-ba44-ae19db09c60e | 1.5468 | -55.8846 | 2024-11-19 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7a5f3e0c-1f3c-357e-9ca5-904bc3ad2211 | -3.9482 | -41.9729 | 2024-11-19 14:10:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 4e3a04a7-dc0b-34de-8ea5-943f53256c2e | -12.5962 | -44.7783 | 2024-11-19 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1e42931e-a4c3-3335-8632-7abc5f32ad2e | -5.223 | -41.8663 | 2024-11-19 14:10:00 | GOES-16 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 5f354cf7-e203-33e7-9eba-23b3648ef8c3 | -10.42 | -44.4705 | 2024-11-19 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 95741554-567d-3a38-b4e7-f9558c8d28a0 | -2.1164 | -55.0654 | 2024-11-19 14:10:00 | GOES-16 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 6011954e-cb17-3fdf-a07b-4ab8286ebd40 | -10.4009 | -44.4731 | 2024-11-19 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 185.1 |
| ff5d7524-47ae-3701-a1cb-5cf91f08d66d | -10.4196 | -44.4937 | 2024-11-19 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4b076d04-c04a-345e-b592-8b3090863e07 | -3.9483 | -41.9491 | 2024-11-19 14:20:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 396396ff-1e8d-307e-bb5a-e11aaa645331 | -10.4009 | -44.4731 | 2024-11-19 14:20:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 33172938-64df-38f2-809b-0e31255aebba | -4.6851 | -41.1112 | 2024-11-19 14:20:00 | GOES-16 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 82.5 |
| d3692466-e721-32af-bf5f-a6eabe077274 | -1.4056 | -52.4166 | 2024-11-19 14:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4c981f28-5a10-32c9-9d0e-ace143bc31d1 | -11.9121 | -44.3727 | 2024-11-19 14:30:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| f2d580f9-9ff7-3d12-978c-ed58984fe538 | 1.5468 | -55.8846 | 2024-11-19 14:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8ec64e5c-d18e-3f4d-b53e-64e3f6b401a5 | -2.4293 | -54.6216 | 2024-11-19 14:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6894b970-d179-3080-a199-ad37a9b45894 | 1.6385 | -55.785 | 2024-11-19 14:30:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0dea6393-a062-3d93-9f03-dae247073763 | -11.9313 | -44.3698 | 2024-11-19 14:30:00 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |


