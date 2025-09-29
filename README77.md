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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f41db9af-02b7-3511-9d85-93133dbc8a67 | -14.57329 | -48.23623 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb8bea8-34f4-3159-b1b8-bf82aff0078c | -11.93099 | -48.03004 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2046991c-9421-3a7b-bb7b-3c464013c648 | -15.25464 | -48.76254 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b2f3d45c-1775-38bf-ac66-2622dd645cb2 | -11.83238 | -51.7855 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3f172bc-786a-3d6c-8b2c-599674bef985 | -13.39141 | -48.15589 | 2025-09-29 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6cf70176-4509-31fc-b9d0-08e86f78739b | -16.84285 | -53.19879 | 2025-09-29 05:27:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26a9b512-ce0d-3d6a-967b-52b0955e4999 | -14.56911 | -48.25769 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70118f78-5592-35bb-894f-a9ab4fa22b2f | -15.43253 | -48.24643 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb9a4851-7a18-3d7f-afa4-57859795c0c9 | -15.18873 | -48.47731 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a0b92c4-f71e-3d4e-a597-d3cd4c181523 | -14.53473 | -48.45261 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 06935223-f765-3e18-88f5-a18ea3d0d56e | -13.57602 | -48.08156 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec9a4bf5-f11a-3233-9b42-8b4a40e67d8a | -14.57416 | -48.27985 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0964c77a-0152-3c1b-9446-3d24800aa3a9 | -11.62445 | -52.84809 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15053995-747c-3d5f-bb6f-3c1140c7cd1f | -15.25529 | -48.75603 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f136d5c-7f1f-3464-8419-925051e360f0 | -14.68304 | -48.16499 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3231c93b-a25c-3ce8-9893-a0d93592f880 | -10.486 | -49.37231 | 2025-09-29 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe394c31-4240-3e85-aa94-a0dd340b5674 | -14.57625 | -48.28168 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ccb02e7-7c02-341f-899a-153d40dc0d10 | -13.74461 | -47.89729 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31a86596-821a-3e07-affe-0d2a1b46dcb5 | -13.74518 | -47.89173 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 021e1b69-89b9-33d7-adbc-bc0b1bfd092e | -14.53547 | -48.44537 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8637f1ac-2d37-3c3a-a842-2cc0ed81cd7f | -15.28225 | -49.50724 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5443ecd7-5b99-34c2-a98e-1bda67d9a0d9 | -13.63347 | -48.05061 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| cf0ce34b-5722-33d0-a94e-a5188a795bcf | -11.92316 | -48.03566 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 37d2f724-41cc-3610-9404-30c6ee5e4568 | -12.45466 | -54.30444 | 2025-09-29 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89fcd7ec-b4a2-37e2-8fe0-b87461cbdf1a | -14.54574 | -48.44808 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4bbc4de3-df2f-3901-815a-f48a8936b74e | -11.83805 | -51.78614 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dae1393d-4477-3f23-b74c-886d0cedad16 | -13.58465 | -48.08931 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb94e244-fa0b-3fcf-923f-41a0a3722a49 | -13.5775 | -48.08774 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a8aaabb-90d8-380d-8b4b-74ba02f2dec1 | -11.82623 | -51.78879 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d370eb6f-6217-3964-ae3e-6ba9c5a56fe1 | -15.28302 | -49.5178 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3c38ded4-9057-3db6-b84d-ebac0615a1a0 | -13.60868 | -48.06905 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27d263bc-0cca-3ba8-a5d8-2c2d3c38e66a | -11.76706 | -47.55697 | 2025-09-29 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 155162d1-dca0-39e4-85c3-b0767e41e738 | -11.92387 | -48.02913 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6a753f96-ce10-30f9-8c77-b94ecd12dcb4 | -15.71722 | -53.64005 | 2025-09-29 05:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2e27d80-4dc1-3ec7-ac53-ac4a5ef4ee2e | -13.75179 | -47.89945 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0541e535-7c4e-394e-a086-515026e1149b | -15.27735 | -49.5056 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1432200a-10ef-359f-a508-1a9b53150abc | -11.62316 | -52.85106 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9989d42b-32e5-31a3-831f-a7a03391a0fc | -13.74581 | -47.89362 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 99b087c3-df69-37fd-95de-b35da42d8cff | -15.70955 | -59.48177 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e73c89f-73e8-30e5-9adf-8b415d1894cc | -15.2188 | -50.11075 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6d163e8-8637-3742-959a-7312b930e86e | -14.53982 | -48.43435 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4225e185-71b1-3cbd-88ff-5424597fbbc2 | -13.62568 | -48.04648 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a619fb1-2e17-37e8-841e-f06da4c82074 | -10.81844 | -47.93884 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2228373b-2310-3dd9-9791-0cc1a60c625d | -13.77219 | -47.91686 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b50a6c1-b385-3ae2-a012-e83b6f259808 | -11.21703 | -47.75006 | 2025-09-29 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17284287-0f24-3f6e-80f6-debe9a0ca71c | -14.67633 | -48.16219 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fba06b56-4255-3ccb-8fbc-1c3708cf0336 | -10.82619 | -47.93359 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f614dcc-08e2-3d27-8ea3-0bda2f1a700c | -14.54914 | -48.45317 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2ebd80c7-fe52-386b-8b71-ae4a823b2841 | -13.62675 | -48.04432 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb855927-5195-36bf-9a5c-7ce24c4f95e3 | -13.38504 | -48.14718 | 2025-09-29 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4b61e276-1419-3731-ad03-84520434cdbd | -15.22048 | -50.09492 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d9dfdee-8818-3799-af61-086e2ec2717c | -10.22035 | -67.04977 | 2025-09-29 05:27:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a20641-ea11-35f3-b9db-782f8275b658 | -17.74921 | -48.76974 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7506503d-9f2d-3eea-ae1c-c2edc6bc930c | -14.57066 | -48.24245 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07705565-3b60-3dde-a5a0-fc3f2b2cd1d6 | -11.62195 | -52.8609 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5118d85-36bd-3104-a476-7c10154f5631 | -13.7586 | -47.91435 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb8716ab-6890-3f3d-8856-71c4e5990794 | -14.53265 | -48.43356 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 950413ef-b4d3-350c-a7a2-9e43f4f2a9c0 | -13.59426 | -48.06688 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ddffb89-753d-3ea2-ad08-781bf3609894 | -14.54635 | -48.44167 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfaf33a3-2f83-3608-9713-634e43ae496d | -13.80634 | -47.95471 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a80e05fd-8298-3902-8ffd-19db67d0c8f1 | -10.47998 | -49.37167 | 2025-09-29 05:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f45076c-69f0-3dcf-99ff-2ae950b877c6 | -15.2611 | -48.76945 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f617460b-8c21-35a8-a69c-5a2c633d354f | -14.68359 | -48.16315 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edb674a3-1168-3e58-a84f-213c46632419 | -15.28404 | -49.50733 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fe98431-c046-3243-8427-053c96e068e5 | -13.00576 | -49.44516 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88e5e793-dce9-31af-b5af-4c4d5c0321da | -11.62922 | -52.84526 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 704b68af-4ead-3f0f-922c-7215f766f0d7 | -13.75198 | -47.90629 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c233419-bfd9-371f-a29e-1e5bd05bf7c9 | -13.65929 | -48.0755 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08bb9be1-c888-3415-9300-66f39fb88186 | -13.79663 | -47.90382 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e4f23c5-175b-36eb-93f4-84f004dbd2e3 | -11.82996 | -51.80499 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ef9b9db-52e2-3bec-9263-64b44a3410f0 | -11.76623 | -47.56457 | 2025-09-29 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d9f5cc1-52b2-33b8-b9bc-4f2b3bd68d11 | -11.83189 | -51.78946 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| df7e0ca4-8687-3a0c-86eb-eec93bb99d0a | -13.01002 | -49.44641 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7226fa30-3d9f-37c7-97f9-2f017007ff60 | -13.80056 | -47.93867 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 83a93e36-8adc-3091-a173-d92a602d8496 | -13.00956 | -49.45062 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41ab2942-90c0-3f29-b78a-389f9fff5f0f | -14.52545 | -48.40121 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42a145d5-1a88-322d-ab4a-9df075804f17 | -11.80171 | -51.80137 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae3b6339-d75a-3496-afe3-94e6dabad6cd | -10.03821 | -52.10707 | 2025-09-29 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1281ce12-9580-3c06-a207-da7441cfe340 | -15.19301 | -48.47913 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b94c004d-65d9-3cb7-bf8b-078e60315521 | -14.5262 | -48.42525 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6899cc14-c149-3869-a960-b46ed0cc0af9 | -15.2852 | -49.49542 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 016a7844-bee5-3914-a920-c87e595fec00 | -14.52165 | -48.39668 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6d9fc3d1-2d2d-3e9d-a20c-4d8cd4334307 | -14.58133 | -48.2287 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e0d7355-1fc9-3004-8ffa-43f022910887 | -14.54509 | -48.45478 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d39b4106-973d-3c98-877b-01a5d1c5d24e | -13.59527 | -48.05699 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1266accc-c4d8-33e9-b6cc-37e670e58717 | -15.29024 | -49.51413 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8bfceca1-698b-3022-b92c-c019ad5a53da | -14.54192 | -48.45309 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12fddb6d-90e4-332b-8654-5a7912f25b27 | -15.27554 | -49.50583 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 701f8e2b-2578-3b0a-9f98-5bc1d1a1bda4 | -10.82108 | -47.93992 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83f74753-ab74-3109-a3fb-c0bfa7cb5d8e | -11.83708 | -51.79396 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 695df6f2-417f-36a4-af76-8be07cf49235 | -15.22541 | -50.10127 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0353bda3-cf9c-39d5-87d1-431945e49fe7 | -15.71193 | -53.63956 | 2025-09-29 05:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe8454f-a8cd-3015-9edb-cfa8055e32b6 | -10.99607 | -57.05656 | 2025-09-29 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abaa058d-171f-3434-855e-806dd22c9dc7 | -14.57247 | -48.2448 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a646fb2-3bee-313c-b541-842c30f6a74d | -15.29078 | -49.50858 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 48c90e69-a1d4-3199-9e9c-242d83397ad5 | -16.02309 | -59.49682 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e017e4a-71bb-3024-b8d9-f6d616d3198d | -10.72265 | -53.7893 | 2025-09-29 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00586014-ace2-329b-95b2-a7512e104311 | -13.63234 | -48.0529 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 038c127f-86a3-391b-8707-713648e5549c | -15.21283 | -50.10454 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3c6b801-6cb6-3948-9334-74f5b3c6f65b | -15.28351 | -49.49509 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README78.md)
