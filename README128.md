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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b17028e8-1d2c-3dc1-8786-17ca17c14d8c | -13.88279 | -44.65703 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 227d62c7-776f-3ef5-9239-236dd9da64c0 | -13.87897 | -44.65208 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7fc8057c-1249-3c07-845d-69ef1c9d4d8b | -13.8784 | -44.65644 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 644c3723-0ee5-3887-a75a-a6a35c04537a | -13.87564 | -44.54029 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 326c1acc-eccb-3d8f-8794-cf0a5db9e59b | -13.87516 | -44.64705 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 041a1afb-75a5-355a-b7e7-918598f48910 | -14.48512 | -44.96061 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fff9611-944b-3918-8dc5-b8205fefeaff | -17.28993 | -56.16805 | 2024-10-09 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 9473aa86-82ac-3fdf-ab9d-6634becbf705 | -13.43512 | -43.20664 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b08d2474-64c9-303d-b687-36e7418ae442 | -13.43447 | -43.21177 | 2024-10-09 04:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 01448d93-06c3-341f-ac0f-072e0bd2e9fc | -12.90817 | -42.76839 | 2024-10-09 04:40:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 85405a89-e90d-3674-8c97-c805de2f0471 | -12.41457 | -42.3405 | 2024-10-09 04:40:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b310c710-7dbb-317d-b4ae-64a4934ad239 | -12.413 | -42.34191 | 2024-10-09 04:40:00 | NPP-375D | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ee2f01a6-84b1-3df8-aaa4-e7d9a87999b9 | -12.40951 | -42.34002 | 2024-10-09 04:40:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b492b82b-ac9a-35cb-a7e6-37177272fa3d | -12.37101 | -42.51796 | 2024-10-09 04:40:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13b3a750-ef2d-3d3e-978e-a19bb59c72fa | -13.81918 | -44.59473 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07c27f66-4d60-3a8f-9e16-83c46827737d | -17.17186 | -51.70607 | 2024-10-09 04:40:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c77e69c-a650-3ff8-bfdc-991b64a4b03e | -17.16853 | -51.70551 | 2024-10-09 04:40:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 264acbae-8f68-30f9-85f8-82d759b223d9 | -17.16413 | -51.68999 | 2024-10-09 04:40:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49ece22a-322b-3013-9788-2cf01007469d | -13.83463 | -44.5792 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5a059f3d-aced-3ed9-be72-af785bcad229 | -13.83407 | -44.58352 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0190781a-58d9-3c12-8ef6-6e280713c5b6 | -13.83352 | -44.58785 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99eb4858-7b38-3518-b3d5-266e05f04050 | -13.83117 | -44.5808 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 07513bb4-41d9-3791-9dff-6f288c0c6a6d | -13.83059 | -44.58511 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 15c1e426-dd22-3408-b3d9-5901908daca0 | -13.83 | -44.58949 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ccdb2b00-133f-395b-9f43-75e3198056fc | -13.82967 | -44.58283 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f9d1058f-c5dc-3f08-9c9b-e7e65ba4cd41 | -13.82912 | -44.58717 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 81db337d-2494-3f73-ade5-b7196ae92b51 | -13.82677 | -44.58009 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 710128c4-0ea2-353f-8f5b-8f3ed7ee6417 | -13.82619 | -44.58443 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c285c4ba-0350-3c1a-857d-5b4141785828 | -13.82499 | -44.59327 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7ef14f17-d86b-34c5-a496-fca7aedcd7fd | -13.81126 | -43.60131 | 2024-10-09 04:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71e4e53b-6a7b-341d-b0e7-94d53a754444 | -13.8106 | -44.60019 | 2024-10-09 04:40:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82f22f63-9f48-3e2c-868a-78f85d8a30e9 | -13.80654 | -43.60069 | 2024-10-09 04:40:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d735d5de-7a21-3f1a-8089-175c18da725f | -13.42299 | -43.80161 | 2024-10-09 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 589a37c2-7c2c-3c91-9a63-bd03f6f5ed3e | -13.41372 | -43.72573 | 2024-10-09 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5cb08d7-d029-38ae-a8d4-f5b59fde5617 | -13.37202 | -43.76793 | 2024-10-09 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51acef45-a476-39ba-8be8-418e10365747 | -13.36808 | -44.77797 | 2024-10-09 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28cb649b-bcfb-34cf-97f8-fe7fda1aa79b | -13.36682 | -44.77977 | 2024-10-09 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56de7e89-c5d3-3535-806f-8f2c69aa1048 | -13.22494 | -45.53537 | 2024-10-09 04:40:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6aae014-c76d-39be-ae7d-00ddf5bb4d18 | -12.88074 | -44.61639 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51f0d0df-cd99-3e7a-b51c-5614200229d9 | -12.87583 | -44.62011 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64dedc58-ecca-307e-8159-665abd85ad04 | -12.87148 | -44.61956 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7665fbc5-6c37-3a6e-be45-0b9b3140dd57 | -12.86769 | -44.61472 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 797bf454-e11a-309a-8988-89327500c086 | -12.86714 | -44.61893 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 993a7af6-ddb8-31c8-80c0-e10dd78cddb8 | -12.37911 | -44.97174 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5f2ddd1-cc54-3f6f-9f5e-1fd7a7f8a4c2 | -12.3787 | -44.97293 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0675ce0b-8483-35a7-8ad5-5e84fc7b9aac | -12.37857 | -44.9758 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0386b4c-2ea2-364c-b55d-f024d8393a99 | -12.37813 | -44.977 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19ef1e5e-2d2e-3f27-a611-96280c745988 | -12.3749 | -44.97112 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5d4073-9c05-3033-973c-8818a465a017 | -12.37449 | -44.9723 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cd107f2-e8eb-37da-b958-baeb962f47f5 | -12.37437 | -44.97512 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b07d1746-1705-310a-b236-0561521789ef | -12.37393 | -44.97631 | 2024-10-09 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ac21924-71f4-39bf-9c6d-146089f2d7f1 | -12.36373 | -44.73612 | 2024-10-09 04:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 136b2dde-b225-3238-880b-2514bc4fe4ad | -12.35945 | -44.73554 | 2024-10-09 04:40:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0d1be1b-5911-383e-a573-f776ae3572ae | -11.92506 | -44.61568 | 2024-10-09 04:40:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e85868a-2eb1-362b-98c2-68c5317250b8 | -11.89242 | -43.88684 | 2024-10-09 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ac288e87-f34a-3684-adcd-d850f1294db4 | -11.89083 | -43.88442 | 2024-10-09 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6269423a-8732-3604-828d-e489d883129f | -11.8902 | -43.88894 | 2024-10-09 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 30151f38-ec2f-3499-b646-df8d4fb07d72 | -11.88792 | -43.88621 | 2024-10-09 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 841b5186-455d-33f2-a180-cb70517ca247 | -11.79435 | -44.49872 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71232ce0-4f52-32c5-a636-0aa4bdf7941e | -11.79381 | -44.50285 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a89699bc-9587-322e-a32a-3fec16b559af | -11.79213 | -44.49994 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7707253-627e-3d59-9d83-b4df9d6b9b89 | -11.79156 | -44.50405 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8be940af-72df-30c2-b9bc-e2f804fe6727 | -11.7801 | -44.52334 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d05bea4-cabd-386b-a9d9-06a75fb88cf5 | -11.77953 | -44.52744 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25bb53e3-f9ca-3368-9648-046fed3ef867 | -11.76415 | -44.21726 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aad386b2-f079-3233-a021-f03480367561 | -11.74043 | -44.49258 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 044c9cd8-6c4a-39ea-93f2-259017cfcf9e | -11.73987 | -44.49671 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fc7267d-a43d-340d-8f71-8f3c417b1583 | -11.73612 | -44.49195 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac8ad8c4-b77a-3328-ad43-f295bff40b6b | -11.73556 | -44.49608 | 2024-10-09 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae9ec2bb-29bf-3e2a-8f68-19b53c5855c7 | -11.65121 | -45.26583 | 2024-10-09 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f8fae02-4fcb-3295-b69c-ee5e4d579e3c | -11.65069 | -45.26955 | 2024-10-09 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de2fe3a7-ffd2-3603-99bd-14550e097820 | -11.64764 | -45.26153 | 2024-10-09 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62ba52ed-eee0-384e-a70a-ae01a3559ef4 | -11.64712 | -45.26529 | 2024-10-09 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9b96495-d5dd-39ac-82ae-c1a1be1a4a24 | -11.64355 | -45.261 | 2024-10-09 04:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7661742f-186f-30db-b9b0-99f5c9f3a580 | -16.21293 | -42.87006 | 2024-10-09 04:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13a72578-821d-31cb-bdcf-1b890333095d | -16.21257 | -42.87318 | 2024-10-09 04:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3aab078f-11f1-385c-8f5a-00ecdac97c56 | -16.21221 | -42.87627 | 2024-10-09 04:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 61ce1551-a318-3505-acc9-095bdbef40e6 | -16.21186 | -42.87931 | 2024-10-09 04:40:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e062d9b1-21fd-3d67-b08c-bf44ff804887 | -16.03906 | -42.85165 | 2024-10-09 04:40:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22854131-589c-3ec5-a60b-4a764cb484f1 | -16.03867 | -42.85494 | 2024-10-09 04:40:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25c2a533-6614-374d-b7ae-6e2688136507 | -16.03432 | -42.84785 | 2024-10-09 04:40:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17cb4146-d025-34e4-b25d-38dc4a829202 | -15.89527 | -43.04049 | 2024-10-09 04:40:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44f0f404-0c6f-3534-a4b7-76a73db3383c | -15.61404 | -42.35852 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6aa1ae0b-7649-36f4-8e67-38c0ec4b3a79 | -15.61368 | -42.3617 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bf07a94-76b6-3cfa-be70-2be0418bebf6 | -15.61264 | -42.3708 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c95586a2-2129-3e33-973b-e2a4d3b01859 | -15.6081 | -42.36389 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 837fdeea-ea83-36ea-a2f9-61acc48c4096 | -15.60774 | -42.36702 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a8933586-c48c-37ed-b51d-db5bdec3aa62 | -15.60738 | -42.37018 | 2024-10-09 04:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92c4803b-87a2-321f-91bb-e1a29c304c3e | -14.71705 | -42.67857 | 2024-10-09 04:40:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4af4a33-3813-3a90-9199-5b570d9634ec | -14.51257 | -43.85063 | 2024-10-09 04:40:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 167aa114-9e8f-3fb9-9f02-ad83bdade720 | -14.51193 | -43.85563 | 2024-10-09 04:40:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6728c774-f589-381c-9ce5-ffc766ecadae | -14.50788 | -43.84999 | 2024-10-09 04:40:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 283d9606-28f7-3aa9-8088-8b8a926d2364 | -14.50725 | -43.85499 | 2024-10-09 04:40:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beef33c5-f6ad-3ad0-9719-1ef82b6e212e | -14.19785 | -45.50835 | 2024-10-09 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ec1a2db-e499-3427-9aaa-ab67ed0c5f60 | -14.19733 | -45.51222 | 2024-10-09 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab6c4b51-b105-3c16-9b1a-d9e2d7cbac9d | -14.18376 | -45.48663 | 2024-10-09 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1799eab5-266c-32fd-81a5-e4e23e362806 | -14.14918 | -44.94023 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67917524-dc93-3ed1-99b1-b2228d1f0206 | -14.14863 | -44.94447 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 699a9703-22d7-3790-88a0-8352ddaffd68 | -14.14107 | -44.93484 | 2024-10-09 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 508348cc-d397-3b07-995a-775addf5fd7f | -14.08865 | -44.14991 | 2024-10-09 04:40:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README129.md)
