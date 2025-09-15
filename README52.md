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
| f8fa2713-a786-3ad7-8feb-68b10a74ae17 | -11.01192 | -51.25041 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 407d19ed-e109-30eb-8b9a-7f395827264e | -14.49722 | -47.34875 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b770fe6e-84d6-3c59-b34a-e1257556c322 | -15.86783 | -47.32472 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ba34674-9b91-3570-b9ae-d9b281f6e70d | -11.79962 | -50.43459 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 56453176-c030-3682-a28a-73bcd36f1113 | -14.49364 | -47.34385 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8efb690-4a8d-3681-b383-c6a44d5e16e4 | -14.47637 | -55.96589 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875afc06-e305-3e48-9d5f-201472d53b9b | -11.85886 | -50.52368 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6506eadd-deb3-385a-8485-048833a7b641 | -14.63592 | -52.01887 | 2025-09-15 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dfe43661-945d-3cc3-a4a5-8314a9868ec2 | -12.24603 | -51.07063 | 2025-09-15 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a39324e6-051f-3b07-8534-093f1f000466 | -11.82991 | -50.44316 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ff215866-c9d6-39d5-b941-6efcd8a0a56e | -11.47987 | -43.60905 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c86f191d-2fef-327f-a729-084291df13c4 | -10.76249 | -50.65133 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dc1418c-da60-348b-9d32-efcc89fe7f64 | -16.66231 | -49.76245 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22cb6aaf-5c60-3501-8a6d-11b75a93e1aa | -16.66903 | -49.76833 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 972a288b-4a74-38a3-9aa1-f4fc2161f4e4 | -11.79505 | -50.44156 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5116816-5c10-37b2-8cfe-5a48fd593c3b | -12.00792 | -46.66473 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e32c2344-9716-3964-a9b2-a993c40d7b11 | -12.44502 | -44.74158 | 2025-09-15 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 465142fc-09ca-31dd-aad7-8544220489fb | -17.34267 | -42.648 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 365908f3-71b9-322b-a065-fa7511378550 | -18.02699 | -46.97276 | 2025-09-15 04:51:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 214090b8-53ec-3a18-9b17-1c98b128cbaf | -17.83379 | -50.42548 | 2025-09-15 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8185a5e9-4844-3aed-afb1-42d15d213816 | -12.00898 | -46.65707 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32fd34d7-d5ba-36f0-a98d-0e819f3ab8d9 | -14.45767 | -55.9668 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b1386ab-5c2e-323b-b424-54541a5099f0 | -16.66533 | -49.76777 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64e6d850-1518-39df-b782-60996670fb27 | -11.80991 | -50.43619 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2f2f2c6a-94fb-34c2-be9d-1b2ec79eb58a | -12.11851 | -44.83159 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9413422c-1338-3e94-90ce-965f2d5fdda2 | -11.86571 | -50.52475 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e369985d-e6e0-3bf5-ae67-1f2b4baab923 | -15.79385 | -52.22296 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ebb217f-8738-3423-b922-33fff1d99c9e | -13.18575 | -47.28096 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de917eec-c70d-3cbc-b937-99b9cfcdf48f | -10.92588 | -61.96563 | 2025-09-15 04:51:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5add3286-6d70-319e-827a-7050b5caf006 | -12.97562 | -47.97364 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a4ef7a6-f2e8-31cb-9782-804aaea17e5d | -15.10785 | -52.48732 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdbcf0db-b728-3c12-abf8-26b2582e1d24 | -13.18479 | -47.28805 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30094777-85bb-3660-88f6-f51063f7114c | -11.07534 | -49.72776 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6a31792-4c36-36ee-ab85-e6845b1a7bb3 | -16.72255 | -54.95797 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e61c464-f513-35e8-9978-b5ec2c3d087d | -14.50653 | -47.34252 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21fd0240-7387-3c88-a305-3a631ec78f36 | -16.28119 | -54.92136 | 2025-09-15 04:51:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c1467942-a21e-343c-b523-cd0648389745 | -11.85714 | -50.51192 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6d485293-e199-3713-9907-2320c6832255 | -15.6698 | -52.23608 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8081ca2-bfbc-3691-a2ae-9409335571a1 | -16.67213 | -49.77308 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d6228b0-ca6e-3843-8984-8cfdd115e328 | -17.33995 | -42.64161 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a34ec898-4a67-372c-a8b2-7d10f0d16b66 | -13.18936 | -47.28512 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49bec965-4606-3d18-84b6-d3755bf82640 | -16.72658 | -54.95475 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e3edf8c-4822-3fec-95fa-47984622506a | -14.20489 | -48.7722 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05d62965-21cc-31ac-b5de-642a0e33c54f | -11.43716 | -43.5345 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b332dfa-0758-3229-bd33-3a4bac4c0a32 | -13.7555 | -48.76989 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2080ec89-a76f-3cab-9d49-2666c662f2e6 | -11.78062 | -46.66411 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d02e8343-8c67-3abb-a2d8-4eb9354cf584 | -9.69501 | -62.00444 | 2025-09-15 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aca871e-702e-3ccf-a9c7-4555de7f86cb | -17.34535 | -42.64686 | 2025-09-15 04:51:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 119dc43f-ac13-34b1-9401-3a17fb5f8c07 | -10.98507 | -55.31494 | 2025-09-15 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 901b6f4d-465b-3f65-9652-f95c250b36e3 | -12.41004 | -63.88963 | 2025-09-15 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ba4ab2e-adec-3fee-a114-b609c3f3a7b8 | -12.04618 | -63.12118 | 2025-09-15 04:51:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e760ead-1600-35a2-b512-1d338d9d18da | -15.0828 | -52.47987 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c4d5ea3-2e9c-3352-9e99-ace93bf9f095 | -12.98341 | -47.97506 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f629757d-261a-31b4-83b7-56a6b5d1c421 | -11.7418 | -50.81313 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfe333f6-ad69-336e-9f41-ac88f468f864 | -11.81276 | -50.44049 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 92858314-a7c4-3115-a742-90249e5ed10d | -10.89082 | -47.78628 | 2025-09-15 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0a0dbd9-cc3a-3860-8348-4f21b694dee4 | -11.29505 | -51.13721 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4695083c-5581-3aea-a705-4c74d0a8228a | -11.45897 | -43.5687 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac1cbd3-10b7-31c1-8a46-5a987ddaef32 | -12.43629 | -63.88547 | 2025-09-15 04:51:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1b74bc3-2b9d-3e38-af66-aa376b625b95 | -16.67712 | -49.77573 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f25ff0e9-6b7c-3e95-9a69-76599d0ea8f2 | -12.97632 | -47.96852 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4b13d9b8-1bb6-32ee-965d-901833c570be | -14.821 | -51.62835 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9960e1a5-2f36-3bdc-841f-91fc51882ac5 | -15.78707 | -53.46133 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c28e85b6-a99e-3fa4-bb5a-2def4c1fcc6c | -14.40511 | -46.39682 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3905e94-3f38-3769-b9cf-f405ee337e4c | -15.78658 | -52.20298 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4419f94d-794e-39ac-a7bd-3272b8eae307 | -10.76305 | -50.64767 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28023ee1-ab5d-3748-b5c0-4caa8d2515a6 | -11.99639 | -46.65512 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 132c75e2-7b71-35a7-b10c-7fe8ab71689f | -14.49888 | -47.33644 | 2025-09-15 04:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f392276-54b8-3f85-b99f-4dbabde0fb5b | -17.83079 | -50.42051 | 2025-09-15 04:51:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 109220db-5b9f-31ed-9c29-2bad334491f0 | -12.00664 | -47.75864 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bfad877-ebac-30bd-9ee7-6dca41fc9e5a | -14.20555 | -48.76754 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 297ddd0c-8868-3eba-8100-a551dc9889f9 | -10.76078 | -50.63985 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f57d941-446f-3b81-824a-ea773ef93a16 | -14.17856 | -46.14445 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb74e05c-5bf1-3262-a25b-e7eed8cbb28c | -12.63416 | -47.9389 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6259a407-4d18-39c3-81bf-b6701cba53a5 | -15.77819 | -52.21283 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f91f611a-9e3c-30df-ac57-df0e237f96c0 | -13.88844 | -48.30608 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 364651b6-546d-33e7-a962-99a66ca0144e | -11.86799 | -50.53278 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75910ce2-01d6-3ff6-a2c6-871b3fa9036e | -15.78155 | -52.21339 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c7607a4-441e-3867-9531-f8ddfb3703cd | -10.92263 | -45.59622 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3a7fbf20-16b1-3eda-8886-5a3bd884becc | -15.69478 | -54.3444 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70aa51e-1e17-30b1-94db-193ee3f7e384 | -11.81334 | -50.43673 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ce37011c-1970-3855-a86e-8e67a1ce79d2 | -14.81705 | -51.6315 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ba814503-ca07-3236-acb0-c88ea3f9979f | -8.45377 | -64.14806 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46e91b3c-e5ab-34bb-8ddf-9d89bfb6e3b9 | -11.50382 | -43.63944 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7600cfff-d1b8-3c6c-846d-49cc2dc7f082 | -16.71638 | -54.95296 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 510fe68d-cf78-3410-9a1d-d29bf03f5a0e | -14.39477 | -52.89573 | 2025-09-15 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| add49447-ace8-3974-8f43-9a7eb3e029fa | -16.66599 | -49.76317 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aee6991-89d2-3955-b70b-253703723921 | -11.27213 | -50.83063 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 033fda6d-7826-348f-99a4-295a7465f803 | -10.92575 | -45.57406 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e28295e-2433-3026-b5f8-65d167d78c1b | -11.16264 | -57.18353 | 2025-09-15 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96e0721e-5154-309b-afb3-86de4a96ec27 | -13.91163 | -44.82574 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4270da7-89b9-341c-a66e-957ae9c5d9bd | -11.71626 | -46.47993 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a6ff2c-9a16-3058-a827-6deb4bc99139 | -11.07707 | -49.71603 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d6e3fc-3db3-339c-9f1d-5135ea34570d | -11.7678 | -50.8022 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 925bb37c-e347-3fbf-a0af-50d87b17df58 | -15.18146 | -52.3219 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30c5b893-5494-3169-bf42-8c92e367e65e | -11.30989 | -50.85519 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e87d39a-289e-350b-9346-0b26d8b1a4a3 | -15.79777 | -52.2199 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 490878b6-303b-3491-b479-7d4ee4b2d08b | -10.98215 | -55.31003 | 2025-09-15 04:51:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 413ac768-8b90-3711-b5a3-0562418d6b87 | -15.42033 | -52.87008 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fa4ec66-56fa-3d0e-8e2f-2038625c400b | -11.00858 | -51.24987 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README53.md)
