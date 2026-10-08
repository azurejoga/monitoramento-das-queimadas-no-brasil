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

## Dados Diários - Página 277

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e23d8c3-97d4-38bf-abce-b3a2192d775f | -10.07975 | -45.68518 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 595193ba-d2fa-314d-84fd-bffdbea65461 | -12.82649 | -45.55789 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6f17b3de-34df-3187-89c6-9ead74e36942 | -14.00318 | -48.7538 | 2026-10-08 16:18:00 | NPP-375 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9d63b518-5d20-3744-8ab1-cf730a508e43 | -11.63204 | -43.70721 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| e242f1a9-2c98-32db-9140-5656c24e7f9c | -10.52121 | -47.31857 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 599c0d7a-3a58-38e7-9d50-52a9de3b3c6b | -10.76005 | -46.59183 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6ad9aa39-65af-3d59-be7a-4c7302e4eda8 | -10.43617 | -47.27824 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 96828eb0-c4ef-35b5-a45e-bc9a33e34300 | -13.73883 | -43.51853 | 2026-10-08 16:18:00 | NPP-375 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ec050fc3-844f-3a06-b0b3-0a7a9537a0d2 | -12.18444 | -44.65485 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 1d20063a-6613-381e-b4b3-402c5da9cff6 | -9.70342 | -45.69439 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| cb8e258e-ddd4-3c5f-a79b-3baea803ca3c | -8.77146 | -47.25752 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 659b983d-d1f0-3f16-8616-a5afd890922a | -11.85695 | -47.37336 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f9eb75cc-9661-351f-84d9-50e442d39eb5 | -8.65539 | -44.87829 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9e96b4f2-d9ac-3d4a-8f41-81b49593d502 | -9.87831 | -44.8711 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 889ef804-cbcc-34bc-9c78-82451a8b7ad2 | -11.45897 | -43.38379 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 71c1562c-0ecb-3ea9-ac64-41511623d8ac | -9.89673 | -44.80723 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 246cca3d-27cc-3a0d-bd04-cfc23647badf | -10.36248 | -42.48595 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 1d4a1d7e-b6aa-3c55-8779-df8b055860af | -10.49857 | -47.30659 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 098f2d2b-1db3-3e33-a60f-3e62ff97d4e3 | -11.45179 | -43.39223 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| acdc14bd-1fe0-361d-b09f-df39627b8e6f | -11.59709 | -43.66933 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8f9d5709-7258-3fb5-84d8-8ee879bf79ff | -14.18014 | -48.66873 | 2026-10-08 16:18:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbb78c12-391c-32d4-b7fe-fb18b5ebae91 | -8.59983 | -44.86747 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c50234c4-0bd4-33b8-a37d-f4e7800d59a8 | -9.90166 | -45.19661 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 536fd072-bdfa-3341-8580-efbc01313fe3 | -11.20746 | -44.86511 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1717196d-4292-3941-9872-9ea609be4da9 | -11.63522 | -43.59823 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| bf3aeb01-bf8b-39df-bc43-f8bb206a261a | -10.45362 | -47.28962 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| eefebf49-8857-34ec-aa63-fc86bdef59bb | -13.13687 | -46.33144 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e1309061-49e9-3619-8aa3-50b71c93f5ed | -9.13488 | -45.85116 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ceafbd66-7210-34c5-b037-9cb16b91d932 | -10.51603 | -47.31734 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 9dd3b4f2-bc28-3ba6-9269-09f14c2f3456 | -11.64971 | -43.68092 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a870b42a-ab42-3c23-bf83-65b7bfff62a2 | -12.18306 | -44.81898 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4bcc0b77-3353-3856-ba90-420a2d03bb83 | -9.78444 | -46.27152 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3de493db-7db0-3d4d-9b38-245bfa53b522 | -12.22375 | -44.74292 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3b845dba-77dc-3820-87fe-2716ee43a1c5 | -12.21356 | -37.80621 | 2026-10-08 16:18:00 | NPP-375 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| daacd648-6f86-358c-a591-a2fdd6bc30c1 | -9.13811 | -45.84013 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 9eef0d8b-5c4e-3dca-99ff-4eac4bacc180 | -9.90318 | -44.78857 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e9e5d312-dc4a-3996-b682-d13844521c65 | -10.07889 | -46.00256 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 848d9307-444d-392b-a0e1-cad0fb532086 | -8.95084 | -45.17646 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 098a6335-4348-3aec-9ea5-7bd1f4709173 | -11.09643 | -43.9989 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| dac8290a-0aa0-3c90-a864-20941ba87e04 | -8.40232 | -38.85444 | 2026-10-08 16:18:00 | NPP-375 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ada1bba6-e6c8-3f7c-9f1f-af8d75f7d5ff | -8.17347 | -44.41301 | 2026-10-08 16:18:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d5023f93-a814-38c4-98d7-0cb0eee1859a | -10.46913 | -47.20271 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d99bd6d-51bd-3040-8212-87b1c23ef673 | -11.39959 | -46.68192 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55978e5e-6854-32da-9fd6-f023023560b5 | -8.95434 | -45.16107 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| d63596f3-b873-3b4a-812e-36dbcb71cd61 | -9.7459 | -46.95518 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcf65b6e-be89-3365-923d-9367d7d1edbd | -8.934 | -45.17739 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f2bcfdce-be8c-3827-88f9-863767febd33 | -10.16704 | -45.96876 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 312576b0-cd45-35b3-870d-c736dc324c27 | -10.43781 | -47.29125 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 79382a92-2e68-3609-a4a5-bac77f79d76c | -12.61915 | -47.89411 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3adc222b-e0f2-35bd-8aca-fb8821b48c78 | -10.42368 | -47.26365 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c7a784c3-a3c8-35b1-9b6a-47988ba96787 | -8.71011 | -47.10763 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708a1ac8-36df-3747-a3d4-8eb1a0e130bc | -8.77187 | -47.26053 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83bc027d-225c-304b-bf55-d0c9081cbd0a | -13.29888 | -41.52242 | 2026-10-08 16:18:00 | NPP-375 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 32e8740c-24de-36d1-a3d4-c544f03f447f | -9.89805 | -44.85062 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0a698136-e211-3e27-b105-1b6168af026b | -9.46372 | -44.61227 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fbeef15-eb32-3802-ae74-4439cf0581bd | -8.97506 | -47.54506 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7ec60fe8-699b-3b4d-88fe-83f09814287d | -13.55836 | -49.15553 | 2026-10-08 16:18:00 | NPP-375 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b71725d9-dfb3-39c3-8f90-9f762dc7bb2f | -8.88613 | -45.39436 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 715a826a-0ec1-3d18-ba51-fc94b8885616 | -8.93078 | -45.18677 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 331.6 |
| 5c1700fd-e1aa-32cb-8e70-279ce9975724 | -8.98851 | -45.94981 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 503327ef-1d0d-3459-861a-95b3b9019f30 | -11.58142 | -43.67925 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| afcfb7ec-c9de-3505-9619-e103c68a759a | -11.85008 | -43.56874 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 912f37a8-6c3a-3b51-8d24-cefe50e5d399 | -11.93774 | -47.21379 | 2026-10-08 16:18:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 393105e1-5ba1-3e7f-98ad-9eb2e2d3e5cd | -9.01292 | -45.13401 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| d84703d2-18bf-3c92-9c42-04565f023ea0 | -10.85808 | -39.24914 | 2026-10-08 16:18:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| ea1be5d1-c366-37f8-8e3e-1d5c75843832 | -9.93583 | -43.57333 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e757bf1b-e12d-34c3-912b-5781d8dc190f | -9.73743 | -46.95197 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c747ff7c-3fa6-32b8-8244-67085f904438 | -10.76153 | -46.60365 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 976de3ae-fbd8-3456-83f6-133bd26bf771 | -13.3694 | -43.86665 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 56b556f4-0a3a-333f-91ca-f3eb67f2fc47 | -9.1013 | -45.13083 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0a0b22f9-e356-38db-a5e1-6659b0f926eb | -9.88179 | -44.85648 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 597c6002-f5c3-37b0-89fa-9d5209112e35 | -8.95816 | -45.15612 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 75439fa5-09c9-371b-8bdb-b688c892a0f8 | -13.70333 | -49.12891 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 3069b641-8e5e-365b-89b1-86b8e5a57511 | -9.83821 | -46.16961 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8945339c-0e92-3cd8-a41f-0bfba4033494 | -9.50873 | -46.84798 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9aafce6e-b4b1-3549-bfcf-d945fcd28591 | -10.41559 | -47.28425 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7c779dcf-8f5c-30c4-81a2-dd1718aac99a | -10.87004 | -45.55375 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 31d5e0dc-469e-35c9-be45-13809eadc3ce | -10.4162 | -47.28397 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f35aea23-8fb7-352c-ac81-539c6ad4e8ff | -11.3093 | -46.68337 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4ae7441d-d8e8-39af-94d3-69ff0ab57d50 | -10.90628 | -45.53896 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 236.5 |
| ab8e7ad6-058d-34cf-9021-f1e2bcf92959 | -11.07738 | -44.01768 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 30e5fdf5-d1ae-36de-b9de-493ca5203f42 | -9.53586 | -45.61884 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a72305f4-bdc1-30a9-9a83-42a60bd3f0f6 | -11.59658 | -43.66556 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3834387d-099f-3ccb-8854-4527bcd6de99 | -12.19339 | -44.82721 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0355eb65-7ef9-3a32-9a68-c70a033caf43 | -11.27549 | -45.20516 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| cc8049d9-928f-36c5-b54d-427fa0bd9912 | -11.62677 | -43.69983 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 202ed86e-f50a-3e31-8fc6-d47fb739523b | -11.58878 | -47.18387 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6db00e15-a97f-374d-8f31-5654d5a3c5eb | -11.76447 | -45.56405 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| a867d874-5338-3f4b-b2ba-886cbd7a6849 | -11.8595 | -48.03372 | 2026-10-08 16:18:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d248adc1-d353-3f8a-92c1-7bf4694adfc8 | -9.76042 | -44.78998 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2200ced3-3f32-3c7f-a941-c82712d49638 | -11.34189 | -46.69498 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 69fd67cf-b0c9-340d-a19b-81496e6a1444 | -11.39981 | -47.57183 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4cc69a6-7320-35dd-aa87-87c16e3fdc98 | -9.7574 | -37.51107 | 2026-10-08 16:18:00 | NPP-375 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6ab05048-0498-3c04-b12e-c6f1d15a6346 | -11.59138 | -43.65853 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 0c45d005-941e-32fc-9631-81ef6e34b813 | -8.33443 | -45.04156 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ec6629ce-2ddc-34cd-be5a-11fc99cb174b | -12.25542 | -44.4199 | 2026-10-08 16:18:00 | NPP-375 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cfa03507-17ad-3e20-82c5-083befc0591f | -11.62313 | -43.6115 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8d92ff5f-6cef-3d2f-b676-f001166bbf6e | -9.10435 | -40.31984 | 2026-10-08 16:18:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 45.2 |
| dde76a9b-cefe-31b1-8524-91f51ba7c4f7 | -9.84873 | -47.85326 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| be8ffe3e-acbb-3d24-891b-727d957e1dca | -11.61534 | -43.61644 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |


[Clique aqui para ver as próximas entradas](README278.md)
