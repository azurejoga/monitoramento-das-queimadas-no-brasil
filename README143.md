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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa64c332-b944-306f-bcf8-1ede10bd3997 | -22.20547 | -47.56226 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e0dbff0f-3393-3072-b227-c8c96f203c62 | -22.52609 | -47.28777 | 2024-09-26 05:01:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de2160ca-44ed-36b7-a04e-e602774a75da | -22.52572 | -47.29192 | 2024-09-26 05:01:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc154510-c332-3a5b-a51f-78a506252757 | -18.03442 | -48.59659 | 2024-09-26 05:01:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7d3fd1c3-1b0c-3408-b099-1d4e5fa071f8 | -18.09793 | -47.98936 | 2024-09-26 05:01:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96be08ca-15bc-3bbc-bcd9-6da2b98d77f0 | -19.27643 | -49.12927 | 2024-09-26 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27b95290-7d9d-377f-918c-2f993d29c0e7 | -19.27551 | -49.1296 | 2024-09-26 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6266390-e906-36b2-93ed-519e5f3309b1 | -18.45009 | -49.21103 | 2024-09-26 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| afeaff8c-6805-37ae-b68a-6de6b5c47250 | -18.44949 | -49.21635 | 2024-09-26 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 65e99898-bdf2-364a-b33f-e5df12d6e4f5 | -18.19841 | -49.11153 | 2024-09-26 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ae9d2f8f-35f1-3206-813f-4a7c98184ca2 | -18.19417 | -49.10653 | 2024-09-26 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 09b8efa7-21ae-30e6-9937-43621f625b1b | -18.19361 | -49.1112 | 2024-09-26 05:01:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 97a3bcb0-a4b6-3c4b-b0d9-f67113b92424 | -18.04365 | -48.60316 | 2024-09-26 05:01:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 95456917-fb3c-3657-8199-206d2deca80f | -18.03936 | -48.59706 | 2024-09-26 05:01:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f70effc3-a60a-3b52-b628-54d4fb812915 | -18.03872 | -48.60265 | 2024-09-26 05:01:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 5b4e1913-e3d2-3c9e-b379-63da08dee4a7 | -18.27826 | -47.81005 | 2024-09-26 05:01:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3746a663-f4cb-35ac-99aa-f0b2f047e5f3 | -19.45936 | -49.14318 | 2024-09-26 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfc7cb21-d1bb-332e-87e7-96e80d9aa2d7 | -19.45514 | -49.13712 | 2024-09-26 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dccca015-f9c0-3b1f-98d5-3e047028b0bf | -19.45453 | -49.14255 | 2024-09-26 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0a002bac-6315-3ab3-bbd2-5b284193e68f | -21.95238 | -48.57128 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d4b8692c-f7fd-3e6d-9f14-9ed2a27d2567 | -21.95205 | -48.57464 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6f359e31-3c10-34cb-a0c6-bffdaf058715 | -21.94719 | -48.57071 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c8c55a4-48af-36cd-8570-0cb7b40bb9b6 | -21.94687 | -48.57402 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| efbec8ee-d751-3d91-8235-4510eb9b776d | -21.93743 | -48.56338 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 76743198-121a-375f-af31-9106c2dcd58b | -21.93711 | -48.56661 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e205bf37-9d31-3ec2-a47d-d0dc3deb1cea | -21.93222 | -48.56295 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 98b27655-7bc2-3f45-ba99-8a2e20819b0a | -21.9319 | -48.56622 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 48500c5e-c690-302d-91c3-254773ff2121 | -21.93159 | -48.56948 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e81a3204-f43f-3753-b861-c7db74d2ac73 | -21.93127 | -48.57271 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c2034d5-06b6-3da4-9483-d2ba410fc5c6 | -21.92703 | -48.56241 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 430ca636-aed4-34f2-bd89-2708ccba09e5 | -21.92671 | -48.56572 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 68694a4f-f29e-3f97-b376-f8a82e6e87d6 | -21.92639 | -48.569 | 2024-09-26 05:01:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80b81ddc-1fbe-32e4-9ec8-248e0e3ff6fd | -22.2173 | -48.67742 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 1c353847-1cbe-31ca-b998-aaa307e683b6 | -22.21696 | -48.68069 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| fe365313-a20d-353c-9c40-72c201a9b801 | -22.21427 | -48.67572 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 8f613c72-cba4-31ea-9204-02e27281cf7f | -22.21395 | -48.67905 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 5faee70c-b2d7-3e93-8623-ddea3e489efb | -22.21217 | -48.67649 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8dc5427a-459d-3050-a95f-a78c645fb23c | -22.21183 | -48.6798 | 2024-09-26 05:01:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 10d40d73-43d8-3052-873c-8549ae9d9f0a | -20.92549 | -49.67915 | 2024-09-26 05:01:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| acb62918-6afe-37d4-9de6-d798681c6743 | -20.92073 | -49.67852 | 2024-09-26 05:01:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1e8f00bd-c488-33da-85a2-51ba831737ae | -23.16721 | -50.01577 | 2024-09-26 05:01:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c94ba102-2463-369c-bfed-f87e0ba2348d | -23.16389 | -49.38717 | 2024-09-26 05:01:00 | NOAA-21 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 082af66d-c617-3f05-bba2-f1512a9bcc6c | -23.15054 | -49.80651 | 2024-09-26 05:01:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fedce5cf-83eb-34c1-aecb-8fddb3373666 | -20.34257 | -50.58232 | 2024-09-26 05:01:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3aba80f9-8c85-38da-99a6-4a804d64829c | -20.33865 | -50.57717 | 2024-09-26 05:01:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ae0789a8-bfde-3712-a4f5-680ad4629bae | -20.33812 | -50.58177 | 2024-09-26 05:01:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4707971f-823e-3fd6-b0a0-8c404112bf81 | -21.27703 | -51.00222 | 2024-09-26 05:01:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 778abdfe-9c42-384d-9210-7d50f5b2cd40 | -21.27264 | -51.00164 | 2024-09-26 05:01:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ec6f8ff-0668-371e-95e0-8694eb654f19 | -23.62876 | -50.88853 | 2024-09-26 05:01:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 30435724-6c8c-3784-a1ed-976a3c8fd0d4 | -23.09046 | -51.20419 | 2024-09-26 05:01:00 | NOAA-21 | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f61c5a46-30ca-3edb-a96f-7c23826c713b | -18.63714 | -51.77814 | 2024-09-26 05:01:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8455a7c6-b397-3989-98bd-d8629d5e1574 | -16.67011 | -50.59887 | 2024-09-26 05:01:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bea62a7-0eaa-3f13-bad8-c23d8bebc098 | -17.91365 | -51.77014 | 2024-09-26 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fafae5e2-3a42-3eae-83fc-c10471138695 | -17.90967 | -51.76947 | 2024-09-26 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2845b49a-c0a3-33c2-974e-971af63ee5a4 | -19.80948 | -51.48436 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f6b95ae1-e822-3cfd-84b4-d4dd336fcf1d | -19.79503 | -51.49862 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4f86b0e-5f94-3062-ba8f-7e116687e74e | -19.79455 | -51.50256 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d5bf399-5f95-3780-a3e8-f8bf8e6cfba7 | -19.79039 | -51.50199 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2878ff58-d4b1-30ef-8e32-1735f799d897 | -19.78719 | -51.49354 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cce9592b-16c8-3262-a280-b80e24583b4a | -19.78671 | -51.49749 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42779963-6e9c-3a1d-a690-5908950e7e12 | -19.78398 | -51.4851 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3559c58b-7974-36e0-a1e2-b98c91a8407d | -19.7835 | -51.48905 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bb9ae572-1ede-36b6-a601-b2ff56eb66f2 | -19.78302 | -51.49299 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a0a6585-7096-3eb9-9442-10d78a93088c | -19.77981 | -51.48454 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| afa97160-1d7e-3672-9ef0-56f476190e1d | -19.77933 | -51.48851 | 2024-09-26 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6617fd51-86c7-35ce-9256-9e8a5300862e | -20.79512 | -51.61761 | 2024-09-26 05:01:00 | NOAA-21 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c1b7fb6b-f21d-3e94-a512-0803dc67d0f1 | -20.61585 | -51.50023 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8d492c15-41bf-3b2b-83cc-bfb7702d5605 | -20.61437 | -51.51832 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 8c46495c-2682-3f49-bc1a-a48914f8d212 | -20.61389 | -51.52236 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0ad1ff6a-49ec-30f2-87c6-4cabe93ef4ec | -20.61384 | -51.51633 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 7a83fadf-0e54-33a8-b726-c49b2c086635 | -20.61334 | -51.52035 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 485e15e5-236e-3cfd-a2b5-f3770f6ce8b5 | -20.61284 | -51.52437 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 8d57a640-7736-389e-b2f5-bf814ee10d11 | -20.61165 | -51.49954 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ab50075-29f9-33c8-9073-f1a0afaa8ef0 | -20.61115 | -51.50361 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a37d8770-a67e-3d1a-9ae5-0c9ddb442087 | -20.61065 | -51.50763 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0c3c4685-6836-35d6-9ff8-4f3d101f72e6 | -20.61015 | -51.51165 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b712e57f-1949-330a-b885-247735c7bfab | -20.60965 | -51.51567 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 0fce9032-0a99-3b75-93e4-751180151d5c | -20.60915 | -51.51969 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| ca8708bd-d333-3761-9aad-8ea667a12e77 | -20.60865 | -51.52372 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 98a282de-b3ec-3c64-9684-f8feb5196a68 | -20.60797 | -51.49472 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 36b5e790-114f-3ab9-a1e4-539c8f8dd160 | -20.60646 | -51.50694 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 12bb2ed2-2ee3-3e31-ba46-02360070e141 | -20.60596 | -51.51098 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 754975b9-d451-33cc-97e3-dc591d8057ba | -20.60546 | -51.515 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 1c6f7b7b-037a-3771-8d98-0c1410acf641 | -20.60496 | -51.51902 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| d1ba0e67-cae8-30e7-9d94-5903dbebca21 | -20.60378 | -51.49404 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 49e8f9b0-a4ae-3c68-b740-85beaa9aca54 | -20.60328 | -51.4981 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f25f2b11-158d-39cf-b28e-fc06532e1ca9 | -20.60277 | -51.50219 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7ff508e4-6003-3d27-ba83-3a05620b333b | -20.60227 | -51.50626 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 39968291-1e57-34be-a67c-4549d4175db8 | -20.60176 | -51.51031 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| aa67171e-e6ff-3154-af93-2b361ee4ece3 | -20.60126 | -51.51435 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 411b93a3-7e3d-3382-a31d-7e8eb6faf935 | -20.59957 | -51.49347 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9014bb4f-51ac-3b86-b684-a55e1d936bdd | -20.59536 | -51.49292 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f107ef4e-956c-36d0-b972-29677217aa64 | -20.59316 | -51.47599 | 2024-09-26 05:01:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3cbeda80-cf6a-3c17-83f7-aa8d382c5225 | -19.11116 | -57.48833 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a78f1bf1-392a-3501-bda6-7626830180cd | -19.13228 | -57.50658 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d3356c61-b6e6-33fd-82e7-1a541cd8dc20 | -19.13168 | -57.51027 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6bdf3c20-06ff-3607-8e5c-ad7c1569f535 | -19.13056 | -57.47321 | 2024-09-26 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5bf40999-e32a-3e57-a801-1d11d272c3b2 | -19.12898 | -57.50598 | 2024-09-26 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b508f58a-6543-3dec-8951-666731cd86f2 | -17.91365 | -53.66763 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c53158ee-0e75-3b14-b30b-6d17642cd1a1 | -17.84862 | -53.69823 | 2024-09-26 05:01:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README144.md)
