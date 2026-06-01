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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84b90fdb-bea4-31fc-8f8e-d5549819f8a6 | -10.71799 | -46.92371 | 2026-06-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ddedd18-c719-3c94-ac0f-7d5a9259ee7c | -12.54734 | -57.17144 | 2026-06-01 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a4f484f-c454-358c-b885-a7ebf0dfa791 | -11.62131 | -52.55688 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8ee7d1b-46b6-3af1-9147-6dd1ddb4ab6f | -11.22181 | -53.82767 | 2026-06-01 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56f65241-3858-3b05-b01f-431eb1ac076c | -10.80531 | -49.39367 | 2026-06-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7831c94a-ccdf-32c6-8905-0b5661c4b73a | -10.80698 | -49.39646 | 2026-06-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d7816c1-3706-3710-929c-70079a6fdc0a | -11.63909 | -52.56944 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dde9a39a-0ac2-36ee-a1f8-fec312c59bea | -7.4557 | -63.79404 | 2026-06-01 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c87037f6-1f97-3b85-930d-d45242d91960 | -8.73358 | -48.32474 | 2026-06-01 05:06:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| facca287-8f22-3c5e-bcec-9fd2f239f793 | -11.7959 | -57.01708 | 2026-06-01 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b31a67ad-27dd-383d-b37e-4c5f3ccb5e4b | -11.74073 | -54.79662 | 2026-06-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88115ba4-21fe-3ac1-9da7-593919d395a4 | -11.79535 | -57.02058 | 2026-06-01 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81bee57b-35b0-319c-9a05-d2fc2d19edc3 | -11.61748 | -52.5563 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e342aa3a-5f73-3647-b7de-6d8393b042a5 | -11.62761 | -52.56767 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13ee10e-7065-33c9-8950-a4e28cb7cfd6 | -13.98511 | -53.87556 | 2026-06-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa367a9a-40c3-372c-8873-f17a191a0641 | -12.06204 | -48.07219 | 2026-06-01 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b76ccb-0737-3e4f-8d7c-d6267c06756f | -13.98877 | -53.87615 | 2026-06-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0eec79ce-10b6-30d4-9f25-570328d53273 | -12.31807 | -47.89879 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8f71fd2-13e8-34e3-aff3-c79ac03fa454 | -11.56825 | -54.59108 | 2026-06-01 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6c62124-7757-37b9-8f3b-88c71f4d4b64 | -12.31768 | -47.90203 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35b7947d-dc0e-3953-87e0-6db2b3bb59c7 | -12.54679 | -57.17495 | 2026-06-01 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f281a3ee-8309-3b79-96ee-79dbcb72f216 | -10.72304 | -46.92829 | 2026-06-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1366a31-891e-37f3-9eb2-d9176f08081e | -10.69754 | -49.61477 | 2026-06-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 300716f6-4f9a-37d9-8f89-4d39bfc7e9be | -11.63978 | -52.56462 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94afb146-bbc3-38be-b7e0-81830d634178 | -11.54867 | -56.33102 | 2026-06-01 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c24af4aa-375e-3583-b339-3ce64cfebe3a | -11.73673 | -54.7999 | 2026-06-01 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e64284be-85d3-3505-a370-6d3d1c025c4a | -11.63144 | -52.56826 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24911ed9-5c63-3f50-89aa-eaf60bde5a89 | -11.61816 | -52.55149 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22e7d5a3-71ff-37c1-b8e3-8268c8311583 | -8.73284 | -48.33028 | 2026-06-01 05:06:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2898cebf-2404-38c2-a7ff-53427da82a13 | -10.57382 | -57.32154 | 2026-06-01 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0194c6b-34c8-32a3-9c2b-f9ab7c66e126 | -11.63526 | -52.56886 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60d50bb8-d34a-37da-9f1e-5211e5dc4ae0 | -10.06771 | -51.664 | 2026-06-01 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08bf0d37-4990-3d1b-8441-46e2e131c1d6 | -11.62829 | -52.56287 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2212f719-2e42-39aa-9f20-e91f090cd3a2 | -9.36936 | -50.54758 | 2026-06-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a223963-53d5-3e94-9fb5-2315d8f05ea9 | -12.06165 | -48.07544 | 2026-06-01 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e526060-3596-35bf-aa2a-e8f46eb9b2e1 | -13.53737 | -49.90363 | 2026-06-01 05:06:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a37e5867-63fd-3945-87f4-ed7b5f58b770 | -11.61433 | -52.55092 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bd866b1-1e66-3e12-a4b3-bfa9172e5028 | -9.25227 | -57.77225 | 2026-06-01 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36c0c39a-433e-3bb9-941d-f4666420b823 | -12.32296 | -47.90269 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb4bedf0-04e7-3568-a1bf-38fb1f2c409e | -12.31728 | -47.90526 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08dfdc10-e02a-3134-b627-918553ced2d0 | -11.61365 | -52.55573 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0985c9db-feae-34ac-b490-d60d8282785b | -11.56537 | -54.58673 | 2026-06-01 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ad13cdb-01d9-3e62-9580-aaaf344dd0a6 | -10.86219 | -46.93917 | 2026-06-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c779d01-1b84-36b9-a33c-6915a0c78a94 | -13.9845 | -53.87999 | 2026-06-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1d067a6-d653-39f2-bb0a-8f9517312ceb | -10.7235 | -46.92455 | 2026-06-01 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9458928-f646-3cf1-bb66-aca51d8a8c86 | -10.81395 | -56.59356 | 2026-06-01 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d79d2365-65dc-3fd3-971b-7179f4fbd8aa | -11.57055 | -54.5757 | 2026-06-01 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88e87cd6-6290-336b-ab3a-377edb2ac06e | -11.7926 | -57.01655 | 2026-06-01 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62a309de-f511-3cf0-994f-90c8cb7b42ce | -10.80935 | -49.39925 | 2026-06-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 731185f8-db84-320d-adc7-a490d405a9b4 | -10.07168 | -51.66457 | 2026-06-01 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39c83756-da35-34f0-a077-c25660f34026 | -12.32257 | -47.90591 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad8b796c-52fa-314c-b952-b6c8d8cc0109 | -11.63212 | -52.56346 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2437786d-51bc-3493-8789-a44b62793466 | -9.37358 | -50.5482 | 2026-06-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d317c09e-d8bc-3462-9acc-eddc32988d42 | -12.5501 | -57.17548 | 2026-06-01 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08e179d9-918f-3431-abca-236a8c04a076 | -11.02275 | -54.32112 | 2026-06-01 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 958c426b-f57f-3ad2-91aa-a1d03ab3ee0e | -20.31194 | -50.54188 | 2026-06-01 05:08:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7474f2ab-569d-3bcb-954e-bd20a09d0369 | -20.3095 | -50.54742 | 2026-06-01 05:08:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 048a3938-ffee-3fea-bcb3-e58fc97d2c49 | -20.31015 | -50.54155 | 2026-06-01 05:08:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f25aefe2-c649-37e0-81b7-a88d2eee24b6 | -20.31133 | -50.54775 | 2026-06-01 05:08:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 79caaff6-0c49-3432-be4e-6cdd4ec4bd05 | -7.5091 | -55.00957 | 2026-06-01 05:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 581730d5-871b-37eb-9843-dfee92665551 | -7.455 | -63.79173 | 2026-06-01 05:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e317efa-62da-3345-8758-95b2eb9b6085 | -7.50207 | -55.00813 | 2026-06-01 05:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcd5867b-8130-3a9f-8d57-f9e7f9ac05cb | -7.4545 | -63.79521 | 2026-06-01 05:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9987e67b-f769-39ca-a4ba-d08f6f92a56d | -12.3177 | -47.90552 | 2026-06-01 06:29:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29cf5af5-a12a-3b0a-bc01-3fe85f82915f | -8.60668 | -47.47116 | 2026-06-01 11:53:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cfbf6330-9771-3332-bd82-f55916f446b5 | -6.64341 | -43.92061 | 2026-06-01 11:53:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ef60e08a-736b-38dc-b3a0-8363daea0ee9 | -6.75688 | -45.02913 | 2026-06-01 11:53:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 834b8d45-9ace-3d4e-bbfa-5464b552caa0 | -6.75822 | -45.01956 | 2026-06-01 11:53:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3bae0ac-c65a-354a-bf65-085726228a8f | -6.89307 | -47.9579 | 2026-06-01 11:53:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c03cdac6-2e19-3ca3-a639-f7cddb16a3b7 | -6.99027 | -42.88029 | 2026-06-01 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 8aada917-277b-37c6-9dd1-2b3e70870e70 | -12.31795 | -47.90338 | 2026-06-01 11:55:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9acf0d7f-4cb4-3665-94a5-bcdbdcc3819a | -10.07127 | -51.66171 | 2026-06-01 11:55:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 56d10383-c004-369a-aa98-5877d36fd30d | -10.46932 | -50.86204 | 2026-06-01 11:55:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 02643281-a9ff-3ddf-a429-8c4233c270e7 | -11.58966 | -47.44146 | 2026-06-01 11:55:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0e7ca605-6a8e-3dc2-8b5d-d55aac6d62ea | -14.05753 | -46.32068 | 2026-06-01 11:55:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cf3446ad-fd7a-3331-9458-281271871d93 | -14.05617 | -46.33072 | 2026-06-01 11:55:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| dc7f8f31-379a-310a-ad72-625359c132bb | -14.05482 | -46.34074 | 2026-06-01 11:55:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61876852-35a7-301b-8f82-32f78e3538ea | -12.42032 | -48.72169 | 2026-06-01 11:55:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a3d0a35-8648-32cb-8781-78b4916ce848 | -10.73121 | -46.92782 | 2026-06-01 11:55:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 35ed40dc-e702-343d-a071-92d7c6c32d3d | -10.72994 | -46.93684 | 2026-06-01 11:55:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 01cb2c52-dbc1-3d67-a80d-ca6521f04bda | -16.6846 | -49.40389 | 2026-06-01 11:57:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc1d8117-e974-33c4-89f5-92cab088a7a8 | -21.63339 | -48.3433 | 2026-06-01 11:57:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 375c30ea-ef38-31cc-b0af-58692f808a49 | -14.76001 | -52.67306 | 2026-06-01 11:57:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d7750dde-3e4d-3fca-b285-d430aa222fd4 | -20.19478 | -49.56561 | 2026-06-01 11:57:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8099c4f6-e7c1-3a97-ac16-67e9db752234 | -20.18595 | -49.56424 | 2026-06-01 11:57:00 | TERRA_M-M | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| a9d51f6e-eab4-3022-ad33-04412650fb10 | -15.01296 | -45.43143 | 2026-06-01 11:57:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 94c92b4a-5926-3c4b-bcc7-bd4ae5e14841 | -21.81252 | -49.12864 | 2026-06-01 11:57:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 8c88a8e3-ae0f-3ba5-8114-6476e3f81aef | -17.70313 | -45.5248 | 2026-06-01 11:57:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d63cd4a5-06b7-3a78-8585-fc3665cdc602 | -14.77058 | -52.67496 | 2026-06-01 11:57:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ced0fde0-3806-3da8-ad7d-d270b9b2e946 | -17.71103 | -53.27728 | 2026-06-01 11:57:00 | TERRA_M-M | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 00a07e94-b920-35b7-b69e-06efb0d307bf | -13.3383 | -52.8844 | 2026-06-01 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5465b967-0ab1-34d2-a6e4-e47a9667ba2f | -12.556 | -57.1798 | 2026-06-01 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7acc8b27-4804-35ec-9309-09812a156f78 | -12.556 | -57.1798 | 2026-06-01 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 44c7d675-a6a5-3126-84a5-45bfe34beade | -12.556 | -57.1798 | 2026-06-01 13:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 220bb49d-391f-3543-841c-854823bc2434 | -12.556 | -57.1798 | 2026-06-01 13:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| bd57d61f-878c-3ba8-a341-6603d0e76d65 | -12.556 | -57.1798 | 2026-06-01 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0f905ec8-7d8f-3c5c-8df2-446d39acf4d0 | -12.556 | -57.1798 | 2026-06-01 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2f35ee51-0d98-3433-91ca-43325ae2fe59 | -12.556 | -57.1798 | 2026-06-01 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 4f7cbd3b-2fdf-30c1-96ee-e8d4d61485ae | -11.6332 | -55.1641 | 2026-06-01 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f43fb489-4e23-3bbc-9df3-532e56fc47a2 | -12.556 | -57.1798 | 2026-06-01 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |


[Clique aqui para ver as próximas entradas](README4.md)
