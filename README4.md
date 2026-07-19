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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356de2e9-4b26-365f-ac7f-f5c28891f2da | -10.8192 | -50.23217 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5841944b-9a91-3448-a279-bcd0a6c9dc1a | -13.66394 | -48.78651 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cc3f568-4e3d-3292-bc86-2b49875fb673 | -17.37443 | -42.72388 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cf1264fb-8a3c-392f-8141-95ca76ffb129 | -11.97656 | -47.11136 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9620cfd0-611f-3c62-b6df-07c52b615559 | -10.82452 | -50.23891 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4528187-cb3c-3a02-9772-e1659d5ae188 | -13.66877 | -48.79133 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 453441bf-31eb-38b4-82ea-8c9a8c933042 | -13.67037 | -48.78347 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a110773d-b787-30fd-839a-2e65964f0444 | -15.70587 | -43.37915 | 2026-07-19 04:02:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6e2615d-2aa3-3739-a674-b3654d0960d4 | -11.38243 | -47.5149 | 2026-07-19 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5f7b566-55ea-3ba9-b939-c714f980259d | -12.65909 | -48.21818 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d779ebbf-e435-3146-9d31-01fb01aa0d05 | -11.77443 | -45.97377 | 2026-07-19 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be24bba2-fe63-30ac-a2d4-e9a4bbf392eb | -12.67078 | -48.21666 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f3de64c-7683-3168-9991-960e3b3fd2d1 | -11.98232 | -47.10925 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 014b31c2-49a5-355d-97a9-73501706e7c6 | -13.56298 | -47.70326 | 2026-07-19 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa05099-cf59-3670-ace8-4103e911aaa0 | -13.67602 | -48.78426 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d072e2a0-f599-3e23-8271-7dbba2253a0d | -10.89931 | -50.33096 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a75a8f6-8c03-313e-b7a0-0cac80b8ea09 | -17.36647 | -42.7269 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 504fac5c-8f38-3843-a767-1e87d2055efb | -17.87017 | -45.54717 | 2026-07-19 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e14743c-c801-3235-93e9-ae664b212e93 | -11.63273 | -47.95353 | 2026-07-19 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb6430be-40a7-3b30-bf4a-a95e033a10c4 | -12.66459 | -48.21922 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4b6e69a-3994-3039-baf1-f00e87fe0f25 | -10.8256 | -50.23354 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95b0b6a5-3ed9-3e5b-8c72-bf7b99b0e3b5 | -17.36721 | -42.72263 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 242dce5e-3475-302b-9809-c1ac7b3a42a9 | -11.96502 | -47.1156 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780f4e52-5ef3-3d92-958e-bfcfb58f0dc4 | -12.6598 | -48.21454 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 131b720c-598b-36a8-9b55-a523af543785 | -13.67678 | -48.78054 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9c2df9d-2a1d-3a60-b7ae-41a9382d44fe | -11.62652 | -47.95618 | 2026-07-19 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d78b4eb-6c36-346e-b77a-940a8f5f3f39 | -17.91384 | -45.27425 | 2026-07-19 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 814bba9e-07ee-3b3c-8400-c8fcd4e7bb82 | -13.62126 | -47.48971 | 2026-07-19 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd6d4511-c42d-33b0-b434-21bc31bc8fa7 | -11.98172 | -47.11242 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45b15258-adf3-35a7-94b6-bee7a443700a | -17.37517 | -42.71962 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0498ff66-9c3f-32a0-b668-56a806e20a03 | -13.67443 | -48.7921 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 58ba8720-6bac-3f7f-bc8d-ecb18cb5eb3e | -11.97019 | -47.11663 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ebc29f0f-07b2-3b1d-b93b-1e85e0e8252b | -12.65838 | -48.22183 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 78713c01-3181-3dbf-b807-39bf622e5dd8 | -17.37156 | -42.71899 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22189d46-ef3e-38af-a3cc-b56cf28050eb | -11.3878 | -47.51594 | 2026-07-19 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1fa05fcb-dffd-39c3-8844-98887d0cfdb5 | -17.37008 | -42.72751 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 81aa6b29-7f13-3684-ba50-9f8b5cce369a | -12.66388 | -48.22285 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18aa337c-6667-30ac-9f60-bf06b9f68f98 | -17.37082 | -42.72323 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27b9b733-4d33-35c7-b497-63db07c640c0 | -13.56228 | -47.7068 | 2026-07-19 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e242d980-7149-31ec-9ff4-b72fa6f339b6 | -10.81812 | -50.23756 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84e0e20f-49be-381a-b7c6-63e569c9675e | -17.37369 | -42.72818 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 416bfc8f-25f7-3bb8-99a7-6f4306f75589 | -16.5447 | -43.76609 | 2026-07-19 04:02:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7612c81d-516e-3ef8-85ba-460533b1c9e5 | -11.9726 | -47.10405 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e10ef014-befa-38d0-81e2-fa637dda65b8 | -14.71927 | -44.66121 | 2026-07-19 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7feabf6c-b30e-36cd-8788-299aa27fbf30 | -11.97716 | -47.10822 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e087ea6-990e-368a-b864-eb36af9280c4 | -11.98688 | -47.11348 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69560e0a-0c96-3d93-990a-91b13025a23c | -13.18458 | -43.55291 | 2026-07-19 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f9f9b2-0cd8-30c7-8b8b-b2338b8fea25 | -14.73806 | -44.67708 | 2026-07-19 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cda2382f-435e-3997-9d91-9402c6ab36a5 | -12.6718 | -48.21086 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9da0650-3668-3bc1-8077-edf9b59342e1 | -11.77344 | -45.9791 | 2026-07-19 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e2065f-9e28-3e96-ad4e-c29b6d75594f | -12.67107 | -48.2145 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 150b8bf9-a4e1-38ab-b424-189455597c4f | -11.97139 | -47.11033 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd4eb6df-45b9-339e-bbee-aaaf17536774 | -11.97199 | -47.1072 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4379695e-aaa3-36bd-9ed3-154259494b1e | -13.67525 | -48.78807 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 03e8b340-f05d-336d-918d-43aeb4712443 | -11.97776 | -47.10506 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f21f0512-be57-30ce-9bae-1c0db6f2c958 | -17.36795 | -42.71838 | 2026-07-19 04:02:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82170314-3d9a-35a2-81b4-f6cce82d45e2 | -12.67148 | -48.21304 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9470f5c7-9180-3dee-8924-9f866eb18804 | -13.66959 | -48.78734 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 109b9962-bf15-3fc3-907c-bfa2f2e9f0fc | -11.97079 | -47.11346 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6456fa01-4f7d-3748-9008-3e22015f4445 | -11.97595 | -47.11451 | 2026-07-19 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e3bf07d-9741-3583-9f89-bfecf5a95738 | -13.67115 | -48.77963 | 2026-07-19 04:02:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d64d369f-76bf-3b6d-85b0-0109e2bc8c2a | -11.76863 | -45.97817 | 2026-07-19 04:02:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e0a5f93-57e5-333c-867c-cb82d2ff3cf2 | -10.81702 | -50.24302 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa990490-0cd6-3422-8546-9b4d8230482b | -22.28732 | -42.59489 | 2026-07-19 04:04:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 446007fc-8392-3383-9772-a0e45e91b84d | -22.2562 | -55.9726 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c69b7437-5aaa-3063-b29a-24e73782141b | -23.67108 | -46.89128 | 2026-07-19 04:04:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3017563c-69fb-3508-b663-4fc5f01970e2 | -21.53247 | -46.76569 | 2026-07-19 04:04:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c784c048-bcde-3557-aca4-b42f40b070c7 | -23.22749 | -46.2377 | 2026-07-19 04:04:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1a96d3ff-8f08-3ffb-9b67-5a5d43a74dea | -22.80022 | -43.54826 | 2026-07-19 04:04:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b24d3fe-95c2-3b4e-8830-4fa9a1c0b34e | -19.74335 | -46.4696 | 2026-07-19 04:04:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d4bd81-74d6-319a-ad80-daf22bca5f2f | -23.75813 | -53.27987 | 2026-07-19 04:04:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e69ee88f-f67f-3bc5-98c6-b70800a64188 | -21.43207 | -41.16887 | 2026-07-19 04:04:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67413d4c-b086-3c2e-a446-45919cf33d35 | -22.90766 | -43.45202 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 89f5a2c5-d8b9-3f0c-aef0-6b6118388f8c | -22.23396 | -55.99978 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e442112d-4854-3ece-bc77-8c85e0f9dfad | -19.98489 | -43.97432 | 2026-07-19 04:04:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fbeca989-c039-3e6d-94e3-2621c17384af | -22.268 | -41.87312 | 2026-07-19 04:04:00 | NPP-375D | CONCEIÇÃO DE MACABU | RIO DE JANEIRO | Brasil | 3301405 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a8332d90-5d31-33c0-826e-c6f678a7c22c | -22.29073 | -42.59556 | 2026-07-19 04:04:00 | NPP-375D | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 894e651e-a7d2-31d1-aec8-ed9470fc56c7 | -22.25404 | -55.98095 | 2026-07-19 04:04:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cf95a2c-c7b9-32bb-913b-ac812dbc4eb6 | -23.37364 | -47.32088 | 2026-07-19 04:04:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 85421415-4f69-3544-9a24-4dab4a2c31aa | -19.98861 | -43.97495 | 2026-07-19 04:04:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 40cbee1b-a07d-3219-9069-7b100f6deec0 | -22.91878 | -43.4322 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b013cd88-4345-3c55-aeae-9f9dad1ef07a | -21.91398 | -41.28255 | 2026-07-19 04:04:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29806c93-6784-3977-a38f-64e572faf849 | -22.91258 | -43.44445 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7072be08-ff08-343c-b44b-a16a68ca20fc | -23.76521 | -53.27692 | 2026-07-19 04:04:00 | NPP-375D | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 7a613f7c-4316-3a37-8d5c-9f8ebb90def1 | -21.53121 | -46.7634 | 2026-07-19 04:04:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 0d5b9ead-f13f-3528-a8c4-d09e4451bbba | -23.45596 | -47.23172 | 2026-07-19 04:04:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e72f3341-c3d1-373c-ae56-afeae77aabed | -19.81519 | -47.96349 | 2026-07-19 04:04:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 429e6ac1-3eca-3aff-a09f-25b8cf909922 | -22.91254 | -43.44713 | 2026-07-19 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 45b47dcc-4f26-3491-88ef-b587cfa3ee93 | -22.46449 | -43.08709 | 2026-07-19 04:04:00 | NPP-375D | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7afd1d5-df8c-392e-8dc2-446084f6602e | -23.72582 | -46.5215 | 2026-07-19 04:04:00 | NPP-375D | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 311130b0-f727-3e5f-9469-520ff87ce96d | -21.5333 | -46.76141 | 2026-07-19 04:04:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1d265f4-9a14-3aa1-a0b6-91b827865261 | -20.65017 | -41.90286 | 2026-07-19 04:04:00 | NPP-375D | ESPERA FELIZ | MINAS GERAIS | Brasil | 3124203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 019b9b6b-49ef-31ba-8d31-73c2cb433e16 | -21.99417 | -56.02935 | 2026-07-19 04:04:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f8f4ad27-8e01-39e0-ad23-bd2b914958bd | -23.36943 | -47.31981 | 2026-07-19 04:04:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aab3c86b-a18b-3bd4-bda5-b79f71a707b3 | -19.81626 | -47.95827 | 2026-07-19 04:04:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1de3d16-8594-327c-9a41-01c8df4db614 | -19.7459 | -46.47091 | 2026-07-19 04:04:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f7c53ae-8d98-35e8-a4fe-975a7b17f2f1 | -22.1899 | -45.82088 | 2026-07-19 04:04:00 | NPP-375D | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 65d15506-c42e-3e82-9271-6062a4b406d0 | -23.72655 | -46.5177 | 2026-07-19 04:04:00 | NPP-375D | SÃO BERNARDO DO CAMPO | SÃO PAULO | Brasil | 3548708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6dac2eb-ba26-3a10-8831-39e37a3d9888 | -21.7411 | -48.60027 | 2026-07-19 04:04:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ade8e5eb-a797-36e7-8b50-84f82a17d19d | -19.93304 | -44.07076 | 2026-07-19 04:04:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README5.md)
